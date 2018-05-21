store
=====

**Initial Commit**

I pushed a drupal commerce , kickstart profile. Includes a pretty comprihensive store set up. It migth have somes stuf we might not need, but good way to get familiar with commerce, how prodcuts (skus/variations) and product displays relate.
Similiar model should be created in fitmoo. We should really just import the product variations. I also added stock module to /sites/all/modules/contrib

We will have to add more modules, for the API, Drupal Services and etc for API end points.

We could keep Kickstart as our base or just start with simple drupal and pick out modules we need.

Base db with sample content is in /db/fitmoo_store.sql

API
=====

**Create User**

Drupal needs to have a user account before user can create/add/edit products to their fitmoo store.
We will also need to create an account for a buyer
Request: 

      - Name
      - email
      - password
      - role -- Store Owner for a user that will be creating and updating products
                people buying prodicts do not need a role, they will have defaul Authenticated user role
      
Return: 

      - uid 
      
Example Call:

      
      ======================REGISTRATION==============================
      POST http://fitmoo.plsekwerks.com/fit_store/user
      Content-Type: application/json
      {
        "name": "testuser",
        "pass": "testuser",
        "mail" : "sabre+1@tut.by"
        "role" : "Store Owner"       
      }
     
      -- response --
      Set-Cookie:  SESSe889a326a5c093a77c387b336cb83f72=E1juSPMd0fUOg3j_esS2G1MwU1jodrDpBjl0KHfli08; expires=Sat, 15-Mar-2014 17:03:45 GMT; path=/; domain=.fitmoo.plsekwerks.com; HttpOnly
      {"uid":"4","uri":"http://fitmoo.plsekwerks.com/fit_store/user/4"}




**Login User**

User needs to be logged in when products are pushed to drupal so products are created as that user.
User needs to be logget in when creating order

Example Call:

          
      ==================LOGIN===================
      POST http://fitmoo.plsekwerks.com/fit_store/user/login
      Content-Type: application/json
      {"username": "testuser","password": "testuser"}
      -- response --
      ["The username <em class=\"placeholder\">testuser</em> has not been activated or is blocked."]
      
      We will setup drupal to auto activate users on API call create user
      
      ==========LOGIN AFTER MANUALY ACTIVATING=============
      POST http://fitmoo.plsekwerks.com/fit_store/user/login
      Content-Type: application/json
      {"username": "testuser","password": "testuser"}
      -- response --
      Set-Cookie:  SESSe889a326a5c093a77c387b336cb83f72=pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM; expires=Sat, 15-Mar-2014 17:09:19 GMT; path=/; domain=.fitmoo.plsekwerks.com; httponly
      {"sessid":"pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM","session_name":"SESSe889a326a5c093a77c387b336cb83f72","user":{"uid":"4","name":"testuser","theme":"","signature":"","signature_format":"filtered_html","created":"1392903024","access":"0","login":1392903359,"status":"1","timezone":"America/Los_Angeles","language":"","picture":null,"data":false,"roles":{"2":"authenticated user"},"rdf_mapping":{"rdftype":["sioc:UserAccount"],"name":{"predicates":["foaf:name"]},"homepage":{"predicates":["foaf:page"],"type":"rel"}}}}
      
      ====================GET TOKEN========================
      GET http://fitmoo.plsekwerks.com/services/session/token
      Cookie:  SESSe889a326a5c093a77c387b336cb83f72=pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM
      -- response --
      frGgOzjJPzrQBHi-5ghxVs43rDtGEVDMxNGjgW717mA
      
      
      Other available USER calls
      
      ===============GET USER LIST==================
      GET http://fitmoo.plsekwerks.com/fit_store/user
      Cookie: SESSe889a326a5c093a77c387b336cb83f72=pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM
      X-CSRF-Token: frGgOzjJPzrQBHi-5ghxVs43rDtGEVDMxNGjgW717mA
      
       -- response --
      [{"uid":"4","name":"testuser","theme":"","signature":"","signature_format":"filtered_html","created":"1392903024","access":"1392903648","login":"1392903359","status":"1","timezone":"America/Los_Angeles","language":"","picture":"0","data":"b:0;","uri":"http://fitmoo.plsekwerks.com/fit_store/user/4"},{"uid":"3","name":"jiri","theme":"","signature":"","signature_format":"filtered_html","created":"1392649287","access":"1392649302","login":"1392649302","status":"1","timezone":"America/Los_Angeles","language":"","picture":"0","data":null,"uri":"http://fitmoo.plsekwerks.com/fit_store/user/3"},{"uid":"1","name":"admin","theme":"","signature":"","signature_format":null,"created":"1391997056","access":"1392903302","login":"1392894035","status":"1","timezone":"America/Los_Angeles","language":"","picture":"0","data":"b:0;","uri":"http://fitmoo.plsekwerks.com/fit_store/user/1"},{"uid":"0","name":"","theme":"","signature":"","signature_format":null,"created":"0","access":"0","login":"0","status":"0","timezone":null,"language":"","picture":"0","data":null,"uri":"http://fitmoo.plsekwerks.com/fit_store/user/0"}]
      
      ===============GET USER==================
      GET http://fitmoo.plsekwerks.com/fit_store/user/1
      Cookie: SESSe889a326a5c093a77c387b336cb83f72=pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM
      X-CSRF-Token: frGgOzjJPzrQBHi-5ghxVs43rDtGEVDMxNGjgW717mA
      -- response --
      {"uid":"1","name":"admin","theme":"","signature":"","signature_format":null,"created":"1391997056","access":"1392903302","login":"1392894035","status":"1","timezone":"America/Los_Angeles","language":"","picture":null,"data":false,"roles":{"2":"authenticated user","3":"administrator"},"rdf_mapping":{"rdftype":["sioc:UserAccount"],"name":{"predicates":["foaf:name"]},"homepage":{"predicates":["foaf:page"],"type":"rel"}}}


**Create Product**

After user creates a product in fitmoo, API call to Drupal to create same product

Request:

    - Product Display name
    - description
    - uid (store owner)
    - type
    - products (these are all the variations created by setting sizes and etc
      - sku (we can autogenerate skus in drupal, these have to be unique)
      - size
      - quantity (stock)
      - image url
      - price
      
Response:

    - sku
    - productID
    
Example API"

      ===============CREATE PRODUCT============== //these are the product variations
      POST http://fitmoo.plsekwerks.com/fit_store/product
      Cookie: SESSe889a326a5c093a77c387b336cb83f72=pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM
      X-CSRF-Token: frGgOzjJPzrQBHi-5ghxVs43rDtGEVDMxNGjgW717mA
      Content-Type: application/json
      {
            "title": "shoes_1",
            "sku": "shoes_1sku",
            "commerce_price_amount": "1000",
            "commerce_price_currency_code": "USD",
            "type": "shoes",
            "field_shoe_size": "10"
      }
      
      -- response --
      {"type":"shoes","product_id":"8","sku":"shoes_1sku","revision_id":"9","title":"shoes_1","uid":"","status":1,"created":1392904311,"changed":1392904311,"commerce_price":{"amount":"1000","currency_code":"USD","data":{"components":[]}},"field_shoe_size":"10","revision_timestamp":1392904311,"revision_uid":"4","log":"","language":"","attribute_fields":["field_shoe_size"],"commerce_price_formatted":"$10.00","field_image_url":null,"commerce_stock":null}
      
      ===============GET PRODUCT==============
      GET http://fitmoo.plsekwerks.com/fit_store/product?sku=shoes_1sku
      Cookie: SESSe889a326a5c093a77c387b336cb83f72=pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM
      X-CSRF-Token: frGgOzjJPzrQBHi-5ghxVs43rDtGEVDMxNGjgW717mA
      -- response --
      {"8":{"revision_id":"9","sku":"shoes_1sku","title":"shoes_1","revision_uid":"4","status":"1","log":"","revision_timestamp":"1392904311","data":false,"product_id":"8","type":"shoes","language":"","uid":"0","created":"1392904311","changed":"1392904311","commerce_price":{"amount":"1000","currency_code":"USD","data":{"components":[]}},"field_image_url":null,"field_shoe_size":"10","commerce_stock":null,"rdf_mapping":[],"attribute_fields":["field_shoe_size"],"commerce_price_formatted":"$10.00","field_shoe_size_entities":{"10":{"tid":"10","vid":"3","name":"6","description":"","format":"filtered_html","weight":"0","vocabulary_machine_name":"shoe_size","rdf_mapping":{"rdftype":["skos:Concept"],"name":{"predicates":["rdfs:label","skos:prefLabel"]},"description":{"predicates":["skos:definition"]},"vid":{"predicates":["skos:inScheme"],"type":"rel"},"parent":{"predicates":["skos:broader"],"type":"rel"}}}}}}
      
      ===============CREATE NODE PRODUCT==========  node product is the main container that holds all variations
      ids = prodct ids from call aboce CREATE product
      
      POST http://fitmoo.plsekwerks.com/fit_store/product
      Cookie: SESSe889a326a5c093a77c387b336cb83f72=pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM
      X-CSRF-Token: frGgOzjJPzrQBHi-5ghxVs43rDtGEVDMxNGjgW717mA
      Content-Type: application/json
      {
            "title": "title21",
            "sku": "sku21",
            "node": "true",  (!!!!!!!!!!STRING!!!!!!!!!! don't need "false" you create simple commerce_product) 
            "description": "description", 
            "type": "shoes",
            "ids": [
                  {
                   "0": "10",
                  "1": "11"
                  }
            ]
      }
      
       -- response --
      {"type":"shoes","title":"title21","uid":"4","status":1,"language":"und","body":{"und":[{"value":"description"}]},"field_product":{"und":[{"product_id":"11"}]},"created":1393331960,"changed":1393331960,"timestamp":1393331960,"log":"","nid":"6","comment":0,"promote":0,"sticky":0,"tnid":0,"translate":0,"vid":"6"}
      
      =================GET NODE PRODUCT============
      GET http://fitmoo.plsekwerks.com/fit_store/node/6
      Cookie: SESSe889a326a5c093a77c387b336cb83f72=pIuj9EEex7MoJ2AEGctHKvFCIFSMcDRTheU2HevpYUM
      X-CSRF-Token: frGgOzjJPzrQBHi-5ghxVs43rDtGEVDMxNGjgW717mA
      -- response --
      {"vid":"6","uid":"4","title":"title21","log":"","status":"1","comment":"0","promote":"0","sticky":"0","nid":"6","type":"shoes","language":"und","created":"1393331960","changed":"1393331960","tnid":"0","translate":"0","revision_timestamp":"1393331960","revision_uid":"4","body":{"und":[{"value":"description","summary":null,"format":null,"safe_value":"description","safe_summary":""}]},"field_gender":[],"field_brand":[],"field_product":{"und":[{"product_id":"11"}]},"rdf_mapping":{"rdftype":["sioc:Item","foaf:Document"],"title":{"predicates":["dc:title"]},"created":{"predicates":["dc:date","dc:created"],"datatype":"xsd:dateTime","callback":"date_iso8601"},"changed":{"predicates":["dc:modified"],"datatype":"xsd:dateTime","callback":"date_iso8601"},"body":{"predicates":["content:encoded"]},"uid":{"predicates":["sioc:has_creator"],"type":"rel"},"name":{"predicates":["foaf:name"]},"comment_count":{"predicates":["sioc:num_replies"],"datatype":"xsd:integer"},"last_activity":{"predicates":["sioc:last_activity_date"],"datatype":"xsd:dateTime","callback":"date_iso8601"}},"cid":0,"last_comment_timestamp":"1393331960","last_comment_name":"","last_comment_uid":"4","comment_count":0,"name":"testuser","picture":"0","data":"b:0;","path":"http://fitmoo.plsekwerks.com/node/6"}
    

**Edit Product**

Any product updates

Request:
  
     - productID
     - price
     - quantity
     - image url
     - size
     - uid
     
Responce:

     - OK
     - productID
     
**Delete Product**

Request:

     - productID
     - uid


Buy Flow
========

User clicks buy now in Fitmoo. Fitmoo makes a request to Drupal to login the user, on successfull return, fitmoo creates a modal window with iframe to call createOrder menu.

Drupal creates order as the loggedin user and displays a checkout form in iframe. User completes the checkout in iframe after confimration page, modal is closed. Confirmation emails go to Buyer and Seller

API
===

**Click Buy - login/register**

Fitmoo if uid then login user, if no uid register user -- see API above.
After register user is logged in

**Create Order**

iframe url request to drupal menu
  example: store.fitmoo.com/createorder/productID/quantity
  
  Drupal add order to cart -> redirect drupal_goto('checkout')
  
  present checkout form (minimal theme)

