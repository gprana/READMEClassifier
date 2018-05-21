# hackathon-2016-12

## Running

#### Locally
* To run: `service/bin/www`
* http://localhost:3000/hotels
* You must set API_KEY environment variable to your Google API key.
* It should pick up proxy settings from http_proxy

#### In GCC
* Latest version not running there yet
* A stub is running here: http://104.198.132.115:8080/

## Docker Notes

1. `scripts/buildit`: Builds the docker image
2. `docker images`: list images
3. `docker rmi <image id>`: remove image
4. `docker run -p 3030:3000 -d <image id>`: Run image mapping private port 3000 to public (external) port 3030
5. `docker ps -a`: show all running containers

#### Reference Docs
* [Dockerizing a Node.js web app](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)

## Google Cloud SDK Notes

1. `google-cloud-sdk/bin/gcloud init`: initialize SDK

#### Reference Docs
* [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs/)

## Kubernetes Notes

1. `scripts/pushit`: Tags and pushes the docker image to my docker registry in GC. If it hangs and can't ping the repo server then likely it's a proxy configuration issue with docker (on the Mac I had to set proxies using Docker preferences).
2. To deploy, go to your [Kubernetes Console](https://console.cloud.google.com/kubernetes/list), click on Conainer Clusters, the click "Connect" for your cluster and follow the instructions to start a local admin dashboard for your cluster
3. Then you can go to [http://localhost:8001/ui](http://localhost:8001/ui)

    Click Pods then Create (in the upper right). To get your image URL you will need to go to the Container Engine Console click on the image in your Registry and click "Show pull command". It will look something like:  us.gcr.io/ecstatic-magpie-152317/server.js:v2. And don't forget to mark the service as external and map your incomming port (Port) to the port the container's port (Target Port)

    After provisioning click on Services and you should see an External endpoints

####  Reference Docs
* [Pushing to Container Registry ](https://cloud.google.com/container-registry/docs/pushing)
* [Creating Single-Container Pods](http://kubernetes.io/docs/user-guide/pods/single-container/)


## Google Places API

1. [Get a key](https://developers.google.com/places/web-service/get-api-key) you can do so using your projects [API Console](https://console.developers.google.com/apis/credentials)
2. Put key in request. Request looks like: 

    `https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&type=lodging&rankby=distance&key=YOUR_API_KEY`


####  Reference Docs
* [Places Web Service Documentation](https://developers.google.com/places/web-service/intro)
* [google-maps-services-js](https://github.com/googlemaps/google-maps-services-js) : Github repo for Node.js client
    * We're not using this due to proxy issues
* [Docs for Node.js google map client](https://googlemaps.github.io/google-maps-services-js/docs/)

