# App Service Mobile completed quickstart for Xamarin.Android apps
This repository contains an Xamarin.Android app project based on the App Service Mobile Apps quickstart project, which you can download from the [Azure portal](https://portal.azure.com). This project have been enhanced by the addition of offline sync, authentication, and push notification functionality. This demonstrates how to best integrate the various Mobile Apps features. To learn how to download the Xamarin.Android quickstart app project from the portal, see [Create a Xamarin.Android app](https://azure.microsoft.com/documentation/articles/app-service-mobile-xamarin-android-get-started/). This readme topic contains the following information to help you run the sample app project and to better understand the design decisions.

+ [Overview](#overview)
+ [Configure the Mobile App backend](#configure-the-mobile-app-backend)
+ [Configure the Xamarin.Android app](#configure-the-xamarin-android-app)
	+ [Set the Mobile App backend URL](#set-the-mobile-app-backend-url)
	+ [Configure authentication](#configure-authentication)
	+ [Configure push notifications](#configure-push-notifications)
+ [Running the app](#running-the-app)
+ [Implementation notes](#implementation-notes)
	+ [Template push notification registration](#template-push-notification-registration)
	+ [Client-added push notification tags](#client-added-push-notification-tags)
	+ [Authenticate first](#authenticate-first)

##Overview
The projects in this repository are equivalent to downloading the quickstart Xamarin.Android app project from the portal and then completing the following Mobile Apps tutorials:

+ [Enable offline sync for your Xamarin.Android app](https://azure.microsoft.com/documentation/articles/app-service-mobile-xamarin-android-get-started-offline-data/)
+ [Add authentication to your Xamarin.Android app](https://azure.microsoft.com/en-us/documentation/articles/app-service-mobile-xamarin-android-get-started-users/)
+ [Add push notifications to your Xamarin.Android app](https://azure.microsoft.com/en-us/documentation/articles/app-service-mobile-xamarin-android-get-started-push/) 

## Configure the Mobile App backend

Before you can use this sample, you must have created and published a Mobile App backend project that supports  both authentication and push notifications (the backend supports offline sync by default). You can do this either by completing the previously indicated tutorials, or you can use one of the following Mobile Apps backend projects:

+ [.NET backend quickstart project for Mobile Apps](https://github.com/azure-samples/app-service-mobile-dotnet-backend-quickstart)

The readme file in this project will direct you to create a new Mobile App backend in App Service, then download, modify, and publish project to App Service.

After you have your new Mobile App backend running, you can configure this project to connect to that new backend.

## Configure the Xamarin.Android app

The app project has offline sync support enabled, along with authentication and push notifications. However, you need to configure the project, including authentication and push notifications, before the app will run properly.

### Set the Mobile App backend URL

The first thing you need to do is to set the URL of your Mobile App backend in the **MobileServiceClient** constructor. To do this, open the ToDoActivity.cs project file, locate the `applicationURL` constant and replace the URL with the URL of your Mobile App backend.
 

### Configure authentication

Because both the client and backend are configured to use authentication, you must define an authentication provider for your app and register it with your Mobile App backend in the [portal](https://portal.azure.com).

1. Follow the instructions in the topic to configure the Mobile App backend to use one of the following authentication providers:

	+ [AAD](https://azure.microsoft.com/documentation/articles/app-service-mobile-how-to-configure-active-directory-authentication/)
	+ [Facebook](https://azure.microsoft.com/documentation/articles/app-service-mobile-how-to-configure-facebook-authentication/)
	+ [Google](https://azure.microsoft.com/documentation/articles/app-service-mobile-how-to-configure-google-authentication/)
	+ [Microsoft account](https://azure.microsoft.com/documentation/articles/app-service-mobile-how-to-configure-microsoft-authentication/)
	+ [Twitter](https://azure.microsoft.com/documentation/articles/app-service-mobile-how-to-configure-twitter-authentication/)

2. By default, the app is configured to use server-directed Facebook authentication. To use a different authentication provider, change the provider by changing the value of the `provider` constant in ToDoActivity.cs and changing it to one of these other values: `AAD`, `Google`, `MicrosoftAccount`, or `Twitter`.

### Configure push notifications

You need to configure push notifications by registering your Xamarin.Android app for Google Cloud Messaging (GCM) in the [Google developer console](https://console.developers.google.com), and then storing the API key in Azure.
This key is used by Azure to connect to GCM to send push notifications.  Assuming that you have already created the notification hub in your backend as instructed in the server project readme, complete the following sections of the push notifications tutorial to configure push notifications:

2. [Register your app for push notifications](https://github.com/Azure/azure-content/blob/master/includes/mobile-services-enable-google-cloud-messaging.md).
3. [Configure the backend to send push notifications](https://github.com/Azure/azure-content/blob/master/includes/app-service-mobile-android-configure-push.md).

Finally, open the ToDoBroadcastReceiver.cs project file and set your Google project number in the senderIDs variable

    public class ToDoBroadcastReceiver : GcmBroadcastReceiverBase<PushHandlerService>
    {
        // Set the Google app ID.
        public static string[] senderIDs = new string[] { "MY_PROJECT_NUMBER" }; 
    }

## Running the app

With both the Mobile App backend and the app configured, you can run the app project.

1. In the Android emulator or device, make sure you have a valid Google account added.

2. Run the app, click the **Sign-in** button and authenticate with the provider. 
	
	After authentication succeeds, the device is registered for push notifications and any existing data is downloaded from Azure.

2. Stop the Windows Store app and repeat the previous steps for the Windows Phone Store app.

	At this point, both devices are registered to receive push notifications.

3. Run the Windows Store app again, and type text in **Insert a TodoItem**, and then click **Save**.

   	Note that after the insert completes, both the Windows Store and the Windows Phone apps receive a push notification from WNS. The notification is displayed on Windows Phone even when the app isn't running.


## Implementation notes 
This section highlights changes made to the original tutorial samples and other design decisions were made when implementing all of the features or Mobile Apps in the same client app. 

###Template push notification registration
The original push notification tutorial used a native WNS registration. This sample has been changed to use a template registration, which makes it easier to send push notifications to users on multiple clients from a single **send** method call. The following code defines the toast template registration:

	// Define a message body for GCM.
	const string templateBodyGCM = "{\"data\":{\"message\":\"$(messageParam)\"}}";
	
	// Define the template registration as JSON.
	JObject templates = new JObject();
	templates["genericMessage"] = new JObject
	{
	  {"body", templateBodyGCM }
	};


For more information, see [How to: Register push templates to send cross-platform notifications](https://azure.microsoft.com/documentation/articles/app-service-mobile-dotnet-how-to-use-client-library/#how-to-register-push-templates-to-send-cross-platform-notifications).

###Client-added push notification tags

When a mobile app registers for push notifications using an Azure App Service Mobile Apps backend, there are two default tags that can get added to the registration in Azure Notification Hubs: the installation ID, which is unique to the app on a given device, and the user ID, which is only added when the user has been previously authenticated. Any other tags that get supplied by the client are ignored, which is by design. (Note that this differs from Mobile Services, where the client could supply any tag and there were hooks into the registration process on the backend to validate tags on incoming registrations.) 

Because the client can’t add tags and at the same time there is not service-side hooks into the push notification registration process, the client needs to do the work of adding new tags to a given registration. In this sample, an `/updatetags` endpoint in the backend lets the client add tags to their push registration. The client calls that endpoint to create new tags, as you can see in the following: 

	try
	{
	    // Define two new tags as a JSON array.
	    var body = new JArray();
	    body.Add("broadcast");
	    body.Add("test");
	
	    // Call the custom API '/api/updatetags/<installationid>' 
	    // with the JArray of tags.
	    var response = await client
	        .InvokeApiAsync("updatetags/"
	        + client.InstallationId, body);
	}
	catch (MobileServiceInvalidOperationException ex)
	{
	    System.Diagnostics.Debug.WriteLine(
	        string.Format("Error with Azure push registration: {0}", ex.Message));
	}

For more information, see [Adding push notification tags from an Azure Mobile Apps client](http://blogs.msdn.com/b/writingdata_services/archive/2016/01/22/adding-push-notification-tags-from-an-azure-mobile-apps-client.aspx).

###Authenticate first
This sample is a little different from the tutorials in that push notifications are send to all devices with push registrations that belong to a specific user. When an authenticated user registers for push notifications, a tag with the user ID is automatically added. Because of this, it's important to have the user sign-in before registering for push notifications. You should also have the user sign-in before executing any data or sync requests, which will result in an exception when the endpoint requires authentication. You also probably don't want an unauthenticated user to see offline data stored on the device. The following button event handler shows how to require explicit user sign-in before push registration and doing the initial data sync:

	[Java.Interop.Export()]
	public async void LoginUser(View view)
	{
	    // Only register for push notifications and load data after authentication succeeds.
	    if (await Authenticate())
	    {
            // Register the app for push notifications.
            GcmClient.Register(this, ToDoBroadcastReceiver.senderIDs);

	        //Hide the button after authentication succeeds. 
	        FindViewById<Button>(Resource.Id.buttonLoginUser).Visibility = ViewStates.Gone;
	
            // Load the data.
            OnRefreshItemsSelected();
        }
	}


