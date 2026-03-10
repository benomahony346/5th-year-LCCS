// external-script.js 

document.write("This message is from an external JavaScript file."); 

function addRow() {
       let table = document.getElementById("dataTable");
       let name = document.getElementById("name").value;
       let age = document.getElementById("age").value;
	   if (age =="" || name ==""){
	      alert("Please put valid information");
		  return false;
		  }
		  else{
		  let row = table.insertRow();
       let nameCell = row.insertCell(0);
       let ageCell = row.insertCell(1);
	   
	   
       nameCell.innerHTML = name;
       ageCell.innerHTML = age;
	   document.getElementById("name").value = ""; 
       document.getElementById("age").value = ""; }
	   // external-script.js 

function showMessage() { 

    alert("Button clicked!"); 
<button onclick="showMessage()">Click Me</button> 
} 
// external-script.js 

function changeContent() { 

    document.getElementById("myParagraph").innerHTML = "Content changed!"; 
<p id="myParagraph">Original content</p> 

<button onclick="changeContent()">Change Content</button> 
} 
  } 