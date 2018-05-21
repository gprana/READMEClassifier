###Read Me

An AngularJS directive for the CKEditor, binding the AngularJS controller to the CKEditor's mark-up, plain-text and configuration options. 

####Getting Started

1. Copy over the file dist/ck-editor.min.js or dist/ck-editor.js

2. Include the path to the direcitve file in index.html
        
        <script src="[your path]/directives/ck-editor.js"></script>
        
3. Include the directive as a dependency when defining the angular app:
        
        
        var exampleApp = angular.module('exampleApp', ['ckeditor']);
        
4. Include the required CKEditor options in the controller:
        
        
        $scope.ckEditorOptions = {
                toolbar: 'full',
                toolbar_full: [
                    {
                        name: 'basicstyles',
                        items: ['Bold', 'Italic', 'Strike', 'Underline']
                    },
                    {
                        name: 'paragraph',
                        items: ['BulletedList', 'NumberedList', 'Blockquote']
                    },
                    {
                        name: 'insert',
                        items: ['Table', 'SpecialChar']
                    },
                    {
                        name: 'forms',
                        items: ['Outdent', 'Indent']
                    },
                    {
                        name: 'clipboard',
                        items: ['Undo', 'Redo']
                    }
                ],
                uiColor: '#FAFAFA',
                height: '400px'
            };
        

5. Reference the directive in the HTML page: 
        
        <textarea ck-editor ng-model="markUp" plaintext="plainText" options="ckEditorOptions"></textarea>
        

See the examples folder for a basic implementation of the directive.


####Requirements
AngularJS - v.1.2.25  
CKEditor - v.4.4.45


#####Credit
This directive is a combination of the various code snippets provided in the answers to the following StackOverflow question with a few of my tweaks added too:

http://stackoverflow.com/questions/18917262/updating-textarea-value-with-ckeditor-content-in-angular-js
