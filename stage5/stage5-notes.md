# Udacity - Intro To Programming Nanodegree
## Stage 5 Notes
---
### 5.2 Lesson 0

#### The Resumes HTML
Web developers have two options, they can hard program a HTML page or they can can use an HTML template and fill it in with data programmatically upon user request.

A template strategy is much better for long term and d

The HTML header element includes script elements that point to the required JavaScript code.

#### CSS and JS in the Resume
JQuery is a JavaScript library that lets you inspect and manipulate elements within a HTML document.

#### Developer Tools
All modern browsers include developer tools that let you inspect various aspects of a website.

The console tool allows you to run basic commands, e.g. console.log(); which is the basic print command for JavaScript. console.log(); is particularly useful for debugging. It's important to remember to include the semi-colon ';' after code in JavaScript.

When console.log(); returns undefined it means that it hasn't created any new data that could be saved. This is good for debugging.

The console can also be used to manipulate local versions of webpages.

#### .append()
JQueries .append() function can be used to add HTML to an element on a page. If the element already has content append will add the new content to the end of the old content.

For example, using the stage5 documents if we wanted to add HTML to the`id="header"` element then we can use the following code. This includes the JQuery selector:
```javascript
$("#header").append([Adam Cardilini])
```

#### Summary
What technologies and techniques have we talked about so far?


* We have spoken about the different coding languages that will be used to create a dynamic resume. These include HTML, CSS and JavaScript, with learning how to use basic javascript being the main focus of these lessons.
* We will be using functions from the javascript package JQuery, and how these tools let us manipulate data in relation to the elements of an HTML page.
* We have spoken about developer tools and briefly explored how these can be used to manipulate website.
* We have touched on the use of console.log for debugging our code.
* We have discussed the use of .append() for adding information to an element of a HTML page.

### Lesson 1 - Data Types
#### Variables
JavaScript saves data in variables. To declare a new variable you need to use `var`, regardless of the type of data you are saving. For example:

```javascript
var firstName = "Adam";
```

We can then check if a variable has been created using `console.log()` and checking the console tool in the developer tools for a browser. For instance, the following code should return 'Adam' in the console of the browser.

```javascript
var firstName = "Adam";
console.log(firstName);
```

Similarly, the following code will return '2'.

```javascript
var add = 1+1;
console.log(add);
```

Even arrays, functions and objects use the same var syntax. We'll explore this in more detail later.

#### string.replace()
We can use the `.replace()` function to replace specified strings within a string variable we are interested in. The following provides and example:

```javascript
var titleTemplate = "Title: articleTitle";
var paperTitle = titleTemplate.replace("articleTitle", "The effects of land clearing on rodent populations");

console.log(titleTemplate);
console.log(paperTitle);
```

#### Add New Data to Your HTML Page
The helper.js file contains several pre-formatted variables with data placeholders, %data%. We want to change the data place holders with our real data.

A simple way to change and then add data to specific pre-formatted variables is to:
1. Identify the variable and the data within it you want to change and what you want to change the data too.
2. Create a new variable by replacing the data placeholder with the required data, e.g. `pre-formattedVariable.replace("%data%", newData)`
3. Then append the new variable to the appropriate element within the HTML document, e.g. `$("#header").append(newVar);`

The following data changes the HTMLheaderName and HTMLheaderRole to include data true for me:

```javascript
var firstName = "Adam";
var lastName = "Cardilini";

var formattedName = HTMLheaderName.replace("%data%", firstName + " " + lastName);
var formattedRole = HTMLheaderRole.replace("%data%", "Associate Lecturer");

$("#header").append(formattedRole);
$("#header").prepend(formattedName);

console.log(formattedName);
console.log(formattedRole);
```

You may have noticed that we use `.prepend()` for addomg the new variables. That's because `.append()` only adds things to the end of an element and we wanted to add our name and role to the beginning of the `#header` element. We can add variables to the beginning of an element by using `.prepend()`.

The order is also important with role first then name, because `.prepend()` will add variables to the beginning of an element in the order that they are coded. This means that formattedName, which is added later, actually is prepended in front of formattedRole.

#### Manipulating arrays in JavaScript
Arrays is javascript are like lists in python. Arrays are created as follows:

```javascript
var arrayName = ["dog", "cat", "rat"]
```

There are several useful functions for manipulating arrays in javascript. A list of these can be
found on the Mozilla Developer Network (MDN) site under [Array][https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array]. A couple of particularly useful functions include:

```javascript
var ages = [27, 29, 30];

// To determine the length of an array
console.log(ages.length);

// Remove the last element of an array and return it.
var kimAge = ages.pop();
console.log(kimAge);
console.log(ages);

// Add elements to the end of an array and returns the array length.
var agesOthers = ages.push(33, 35);
console.log(agesOthers);
console.log(ages);
```

#### Manipulating strings in JavaScript
There are several useful functions for manipulating strings in javascript. A list of these can be
found on the Mozilla Developer Network (MDN) site under [String][https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String]. A couple of particularly useful functions include:

```javascript
// To access characters is a string
return 'string'.charAt(2); // returns 'r'
return 'string'.charAt[2];

// To change the case of a string so the following string is Adam CARDILINI.
var name = "adAm CaRDiLiNI";
console.log(name);

var names = name.split(" ");
console.log(names);

var firstName = names[0].toLowerCase();
console.log(firstName);

var lastName = names[names.length - 1].toUpperCase();
console.log(lastName)

```

The two pieces of code both convert a name to have a standard format 'First LAST'. The first piece of code is one that I wrote, the second piece of code is what the course provided as the answer.

```javascript
// My code
var name = "AlbERt EINstEiN";

function nameChanger(oldName) {
    var finalName = oldName;

    // Split name into an array to work on first and last separately
    var names = finalName.split(" ");

    // Convert first name to lower case and then first letter of the name to upper case
    var firstName = names[0].toLowerCase();
    firstName = firstName[0].toUpperCase() + firstName.slice(1, firstName.length);

    // Convert last name to upper case
    var lastName = names[names.length - 1].toUpperCase();

    finalName = firstName + " " + lastName;
    return finalName;
};

// Did your code work? The line below will tell you!
console.log(nameChanger(name));

// Their code
function nameChanger(oldName) {
    var finalName = oldName;
    var names = oldName.split(" ");
    names[1] = names[1].toUpperCase();
    names[0] = names[0].slice(0,1).toUpperCase() + names[0].slice(1).toLowerCase();
    finalName = names.join(" ");
    return finalName;
}
```

There code is much simpler an cleaner. They manipulate the array elements rather than creating new variables, the chain functions and they use the `join()` function which is nice.

#### Object literal notation
Javascript dose not include classes, it only has objects. The following code creates an object because the curly braces indicate we are using object literal notation.

```javascript
var bio = {
  "name": "Adam";
  "age": 29;
  "skills": python;
};
```

If we then wanted to access particular properties of an object and append it to a page we would use the following code:

```javascript
var bio = {
  "name": "Adam",
  "age": 29,
  "skills": python
};

$("#main").append(bio.name);
```

It's possible to add new properties to an object using dot notation or bracket notation. For example, if I wanted to add my email to the bio object I could do the following:

```javascript
// Dot notation
bio.email = "a.cardilini@gmail.com"

// Bracket notation
bio["email"] = "a.cardilini@gmail.com"
```
This doesn't require the creation of a new variable.

#### JSON
JSON (JavaScript Object Notation) is a format for transferring and storing nesters or hierarchical data, meaning that objects (or other types of data) can be embedded in other objects. [This][https://www.copterlabs.com/json-what-it-is-how-it-works-how-to-use-it/] is a good explainer of JSON.

We can create JSONs using a mix of nested square and curly brackets which can lead to easy mistakes. Luckily there are software called JSON linter that check your JSONs and find any pesky syntax errors, e.g. [jsonlint.com][http://jsonlint.com/]. The Atom text editor also highlights errors which is helpful.

```javascript
// Examples of JSONs
// Simple JSON and access
var adam = {
  "age" = "29",
  "city" = "Melbourne, Vic",
  "gender" = "male"
};
console.log(adam.age)

// JSON arrays
var family = [{
  "name" = "Adam",
  "age" = "29",
  "gender" = "male"
},
{
  "name" = "Jess",
  "age" = "27",
  "gender" = "female"
}];
console.log(family[2].name); // output: Jess

// Nesting JSON data
var family = {
  "adam": {
    "name" = "Adam",
    "age" = "29",
    "gender" = "male"
  },
  "jess" = {
    "name" = "Jess",
    "age" = "27",
    "gender" = "female"
  }
};
console.log(family.jess.name) // output: Jess
```

JSON is important because it allows us to quickly and asychronously load data without having to re-render a page.
