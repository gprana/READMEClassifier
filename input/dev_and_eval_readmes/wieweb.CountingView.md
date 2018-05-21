# CountingView

![Carthage compatible](https://img.shields.io/badge/Carthage-compatible-4BC51D.svg?style=flat)
![Swift 2.2](https://img.shields.io/badge/Swift-2.3-orange.svg)

Inspired by [UICountingLabel](https://github.com/dataxpress/UICountingLabel) this is a swift version of an animated counting label.

![Example](Resources/Example.gif)

##Usage

To start the counting animation just call ```startCounting```

	label.startCounting(destinationValue: 100)
	
	// with all available properties
	label.startCounting(0,
   			destinationValue: 1000,
          	duration: 3,
	          method: .Linear,
   		       progress: { value in
       		   	print(value)
          	},
          	completion: {
          		print("complete")
        	})
	
### Format

By setting ```format``` you can also add a text.

	label.format = "%@ Value"
	
Alternatively you can provide a ```NSNumberFormatter``` to define the format of the animated number.

        let formatter = NSNumberFormatter()
        formatter.minimumIntegerDigits = 5
        formatter.maximumFractionDigits = 0;
        formatter.numberStyle = .DecimalStyle
        formatter.groupingSeparator = "."
        
        linealLabel.numberFormatter = formatter

### Custom AnimatedView

If you want to create your own animated views use the ```CountAnimator```class. 

	let animator = CountAnimator(startValue: startValue, destinationValue: destinationValue, duration: duration, method: method)
	
	animator.startCount({ value in
		if let formatedValue = self.numberFormatter.stringFromNumber(value) {
			self.text = String.localizedStringWithFormat(self.format, formatedValue)
			if let progress = progress {
				progress(value: value)
			}
		}
	}, completion: {
		if let completion = completion {
			completion()
		}
	})
	        
This class also provide ```startCount``` with a ```progress```and ```completion```closure.


## Installation

#### Carthage

Add the following line to your [Cartfile](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile).

####Swift 2.3

```
github "wieweb/CountingView" ~> 1.1
```

####Swift 3.0

```
github "wieweb/CountingView" "swift3.0"
```

Then run `carthage update`.

#### Manually

Just drag and drop the two `.swift` files in the `CountingView` folder into your project.

## Todo

* Counting Button

