calendarjs
==========

A simple jquery events calendar plugin

How to install
--------------

1. Download the zip and extract it
2. Acess the index.html to see a demo
3. If you wanna run the tests suite run tests.html

How to use it
-------------

Basic usage
```
<!DOCTYPE html>
<html>
  <head>
    <title>CalendarJS</title>
    <meta charset="utf-8">
  </head>
  <body>
    <div class="calendar"></div>

    <script src="https://code.jquery.com/jquery.js"></script>
    <script src="calendar.js" charset="UTF-8"></script>
    <script>$(".calendar").calendarjs()</script>
  </body>
</html>
```

How to translate
----------------

```
// localization object in PT_BR
var pt_br = {
  month_names: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
           'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
  weekdays: ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
  weekdays_short: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
}

$(".calendar").calendarjs({l10n: pt_br})
```

Complete API
------------

* ```set_date(dateObject)``` - set the calendar date

  Ex:  
  ```$("calendar").calendarjs().set_date(new Date(2013, 1, 1))```
  
* set_events(eventList) - Set an event list

  **IMPORTANT**: eventList should be ordered by date!
  
  Ex:  
  ```
  evtList =  [
    {
      date: new Date('2013', '10', '01'),
      object: {'title': 'My first event', 'desc': 'First event'},
    },
    {
      date: new Date('2013', '10', '01'),
      object: {'title': 'Second event on day 01', 'desc': 'Second event on day 01'},
    },
    {
      date: new Date('2013', '10', '02'),
      object: {'title': 'Sencond Event', 'desc': 'Second event'},
    },
  ]
  
  $cl = $('div.calendar').calendarjs()
  
  $cl.set_events(evtList)
  ```
  
  PS: Calendar will set the current display month to the month of the first event on list.
  

Options
-------

* ```width: 400``` -  The with of the calendar, always in px
* ```height: 230``` - The height of the calendar, always in px 
* ```auto_render: true``` - Should render calendar automatically when you cal $.calendarjs()
* ```l10n: dflt_l10n``` - An object which have localized strings
* ```date: new Date()``` - The calendar start date
* ```short_weekdays: true``` - Which format of weekdays should calendar use
* ```next_link: '<a href="#"> >> </a>'``` - Link to the next month
* ```prev_link: '<a href="#" class="prev"> << </a>'``` - Link to the previous month
* ```day_click_cb: function(cl, date, evtList){}```  

  Callback function called when user click in a day, this function recieves:  
  the calendar object, the date in format dd/mm/yyyy and the list of events  
  or the Event object (if the clicked day have just 1 event)

* ```month_change_cb: function(old, new){}```  
 
  Callback function called when month change, this function recieves:  
  The old_date and the new_date

  
