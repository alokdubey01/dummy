function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }


//   const themeToggle = document.querySelector(
//     '.theme-switch input[type="checkbox"]'
//   );
//   // Function that will switch the theme based on the if the theme toggle is checked or not
//   function switchTheme(e) {
//     if (e.target.checked) {
//       document.documentElement.setAttribute("data-theme", "dark");
//     } else {
//       document.documentElement.setAttribute("data-theme", "light");
//     }
//   }
//   // Add an event listener to the theme toggle, which will switch the theme
//   themeToggle.addEventListener("change", switchTheme, false);

//   function switchTheme(e) {
//     if (e.target.checked) {
//       document.documentElement.setAttribute("data-theme", "dark");
      
//       // Set the user's theme preference to dark
//       localStorage.setItem("theme", "dark");
//     } else {
//       document.documentElement.setAttribute("data-theme", "light");
      
//       // Set the user's theme preference to light
//       localStorage.setItem("theme", "light");
//     }
//   }
//   const currentTheme = localStorage.getItem("theme");
// // If the current local storage item can be found
// if (currentTheme) {
//   // Set the body data-theme attribute to match the local storage item
//   document.documentElement.setAttribute("data-theme", currentTheme);
// // If the current theme is dark, check the theme toggle
//   if (currentTheme === "dark") {
//     themeToggle.checked = true;
//   }
// }


function readURL(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function(e) {
          $('#imagePreview').css('background-image', 'url('+e.target.result +')');
          $('#imagePreview').hide();
          $('#imagePreview').fadeIn(650);
      }
      reader.readAsDataURL(input.files[0]);
  }
}
$("#imageUpload").change(function() {
  readURL(this);
});