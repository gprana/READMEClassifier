Carrierwave Base64 Storage
==========================

This is the storage for Carrierwave that serializes the file and saves it into
the field the uploader was mounted on.


Installation
------------

    gem 'carrierwave-base64-storage'


Usage
-----

In your uploader specify the storage:

    class AvatarUploader < CarrierWave::Uploader::Base
      storage :base64
    end

IMPORTANT: When you mount the uploader on a `field`, it uses `field_data` attribute
on the model to store the actual data, and so make sure the field exists
in your model and is able to fit long text blobs (`TEXT` in SQL).

Example for the ActiveRecord:

    class User < ActiveRecord::Base
      mount_uploader :avatar, AvatarUploader
    end

(It will be using `avatar_data` for the actual data and the content type.)


License
-------

Copyright (c) 2008-2012 Aleksey Gureiev

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
