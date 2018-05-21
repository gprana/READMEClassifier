angular-duration-format
===================

AngularJS filter for formatting duration.

## Usage ##
Add `angular-duration-format` as your app dependency.

```
  angular.module('myModule', [
    angular-duration-format'
  ]);
```

In templates you can use
```
  <p>
    Time passed: {{ passed | duration:'hh:mm:ss:sss' }}<br/>
    Preformatted: {{ passedPre }}
  </p>
```

In controllers (or directives, services, anywhere)
```
  angular.module('myModule').controller('exampleCtrl', function($scope, $filter) {
    var durationFilter = $filter('duration');
    
    $scope.passed = 123456789;
    $scope.passedPre = durationFilter($scope.passed, 'hh:mm:ss:sss');
  });
```

The result should be the same in both cases:
```
  Time passed: 34:17:36:789
  Preformatted: 34:17:36:789
```

## Format options ##
Available formatting options:
 * (y)ear
 * (d)ay
 * (h)our
 * (m)inute
 * (s)econd
 * `sss` for milliseconds

Each number will be zero-padded to two places if you double letters (ex. `hh`, `mm`). Milliseconds are exception - they are padded to four places and you have to pass four letters (`ssss`).

You can use every separator you want, but be careful. Passing format `h hours, m minutes` will produce unexpected results `34 34ours, 17 17inutes`. To avoid that, wrap every separator containing reserved letters in quotaion marks, like that `h 'hours', m 'minutes'`. (remember about escaping them in your code!). Now, the result should be nicely formatted `34 hours, 17 minutes`.

## Additional notes ##
Note, that you can ommit some unit "levels", but it can produce weird results. If in example above you change format to `hh:ss`, result will be `34:1056`, because 17 minutes and 36 seconds it is 1056 seconds.
 
