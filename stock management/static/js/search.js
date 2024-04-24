document.addEventListener("DOMContentLoaded", function() {

    const dropdowns = document.querySelectorAll(".dropdown");
   
   
   
    dropdowns.forEach(function(dropdown) {
   
     const searchInput = dropdown.querySelector(".search-input");
   
     searchInput.addEventListener("click", function(event) {
   
      event.stopPropagation();
   
     });
   
   
   
     dropdown.addEventListener("click", function() {
   
      this.classList.toggle("show");
   
     });
   
   
   
     document.addEventListener("click", function(event) {
   
      if (!dropdown.contains(event.target)) {
   
       dropdown.classList.remove("show");
   
      }
   
     });
   
    });
   
   });
   
   