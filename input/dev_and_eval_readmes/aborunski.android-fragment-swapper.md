# FragmentSwapper
FragmentSwapper is an Open Source Android library that allows easy fragment's management. It is somewhat similar to Activities management model.
For instance, new fragment can be launched from another one with action's request (using request code) and then recieve the result.

FragmentSwapper works with Android Support Library.

In order to manage multiple fragments, FragmentSwapper object is required.

Each fragment must implement FragmentDescriptor interface. Its example implementation is provided in BaseFragment class. BaseFragment can be also used as a base class in your application.

Currently, it is possible to manage fragments within one container, using SingleContainerFragmentSwapper class.

For information how to initialize the SingleContainerFragmentSwapper, and how to implement fragment swapping please check sample application and the library code.

### Project integration

Add repository reference in your build.gradle file:


repositories {
    ...
    maven {
        url 'http://dev.open-rnd.net:30844/content/groups/public/'
    }
    ...
}


Add library dependence:


dependencies {
    compile group: "pl.openrnd.android", name: "fragmentsswapper", version: "1.0.1"
}


### License

2015 (C) Copyright Open-RnD Sp. z o.o.

Licensed under the Apache License, Version 2.0 (the "License");<br />
you may not use this file except in compliance with the License.<br />
You may obtain a copy of the License at<br />

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software<br />
distributed under the License is distributed on an "AS IS" BASIS,<br />
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.<br />
See the License for the specific language governing permissions and<br />
limitations under the License.
