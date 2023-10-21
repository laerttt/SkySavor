///////////////////////////////////// - MAP - ///////////////////////////////////////////////
// Get all path elements within the SVG
const paths = document.querySelectorAll("path");

// Function to change CSS variables based on class
function updateCSSVariables(className) {
  const root = document.documentElement; // Get the root HTML element

  switch (className) {
    case 'europe':
      root.style.setProperty('--europe_stroke', 'black');
      root.style.setProperty('--europe_width', '1');
      root.style.setProperty('--europe_fill', 'rgb(97, 136, 187)');
      break;
    case 'northAmerica':
      root.style.setProperty('--northAmerica_stroke', 'black');
      root.style.setProperty('--northAmerica_width', '1');
      root.style.setProperty('--northAmerica_fill', 'rgb(97, 136, 187)');
      break;
    case 'southAmerica':
      root.style.setProperty('--southAmerica_stroke', 'black');
      root.style.setProperty('--southAmerica_width', '1');
      root.style.setProperty('--southAmerica_fill', 'rgb(97, 136, 187)');
      break;
    case 'asia':
      root.style.setProperty('--asia_stroke', 'black');
      root.style.setProperty('--asia_width', '1');
      root.style.setProperty('--asia_fill', 'rgb(97, 136, 187)');
      break;
    case 'africa':
      root.style.setProperty('--africa_stroke', 'black');
      root.style.setProperty('--africa_width', '1');
      root.style.setProperty('--africa_fill', 'rgb(97, 136, 187)');
      break;
    case 'oceania':
      root.style.setProperty('--oceania_stroke', 'black');
      root.style.setProperty('--oceania_width', '1');
      root.style.setProperty('--oceania_fill', 'rgb(97, 136, 187)');
      break;
    default:
      // Reset the CSS variables for other classes or when no class is found
      root.style.setProperty('--stroke', 'black');
      root.style.setProperty('--width', '1');
      root.style.setProperty('--fill', 'rgb(97, 136, 187)');
      break;
  }
}

// Function to reset CSS variables based on class
function resetCSSVariables(className) {
  const root = document.documentElement; // Get the root HTML element

  switch (className) {
    case 'europe':
    case 'northAmerica':
    case 'southAmerica':
    case 'asia':
    case 'africa':
    case 'oceania':
      // Reset the CSS variables for the specific classes
      root.style.removeProperty('--europe_stroke');
      root.style.removeProperty('--northAmerica_stroke');
      root.style.removeProperty('--southAmerica_stroke');
      root.style.removeProperty('--asia_stroke');
      root.style.removeProperty('--africa_stroke');
      root.style.removeProperty('--oceania_stroke');

      root.style.removeProperty('--europe_width');
      root.style.removeProperty('--northAmerica_width');
      root.style.removeProperty('--southAmerica_width');
      root.style.removeProperty('--asia_width');
      root.style.removeProperty('--africa_width');
      root.style.removeProperty('--oceania_width');

      root.style.removeProperty('--europe_fill');
      root.style.removeProperty('--northAmerica_fill');
      root.style.removeProperty('--southAmerica_fill');
      root.style.removeProperty('--asia_fill');
      root.style.removeProperty('--africa_fill');
      root.style.removeProperty('--oceania_fill');
      break;
    default:
      // Reset the CSS variables for other classes or when no class is found
      root.style.setProperty('--stroke', 'black');
      root.style.setProperty('--width', '1');
      break;
  }
}
// Add mouseenter and mouseleave event listeners to each path
for (let i = 0; i < paths.length; i++) {
  const path = paths[i];
  let className;

  path.addEventListener('mouseenter', () => {
    // Get the class name of the hovered path
    className = path.getAttribute('class');

    // Update CSS variables based on class
    updateCSSVariables(className);
  });

  path.addEventListener('mouseleave', () => {
    // Reset CSS variables using the stored class name
    resetCSSVariables(className);
  });
}

        // Function to handle path click event
        function getPathClassName(event) {
          const path = event.target;
          const h1Element = document.getElementById("test");
          if (path.tagName === "path") {
              const className = path.getAttribute("class");
              h1Element.textContent=className;
          }
      }

      // Attach click event listener to all SVG paths
      const svgPaths = document.querySelectorAll("svg path");
      svgPaths.forEach(path => {
          path.addEventListener("click", getPathClassName);
      });

/*----------------------POPUPS----------------------*/

/*Visited places color*/ 
// Define your countries object
let countries = {
  "USA": "NorthAmerica",
  "France": "Europe",
  "China": "Asia",
  "Brazil": "SouthAmerica"
};

// Function to set initial fill colors for countries on the SVG map
function setInitialFillColors() {
  for (let country in countries) {
      let continent = countries[country];
      let svgElement = document.getElementById(country);
      if (svgElement) {
          svgElement.style.fill = "lightblue";
      }
  }
}

// Call the function when the page finishes loading
window.onload = function() {
  setInitialFillColors();
  // You can add more code here if needed
};

/*Kilometers popup*/
function popupkm(event) {
  const path = event.target;
  const continent = path.getAttribute("class");
  const popup = document.getElementById(`${continent}-popup`);
  const popupContent = popup.querySelector(`.${continent}-fraction`);

  let countries = {
      "USA": "northAmerica", // Corrected continent names
      "France": "europe",
      "China": "asia",
      "Brazil": "southAmerica",
      "Albania": "europe"
  };

  let continentCounts = {
      "europe": 0,
      "asia": 0,
      "northAmerica": 0,
      "southAmerica": 0,
      "oceania": 0,
      "africa": 0
    };

  for (let country in countries) {
      let continentName = countries[country];
      continentCounts[continentName]++;
  }

  const continentMaxCapacity = {
      "europe": 44,
      "asia": 49,
      "northAmerica": 23,
      "southAmerica": 12,
      "oceania": 14,
      "africa": 54
      // Add other continents as needed
  };
  for (let country in countries) {
    let continent = countries[country];
  
    let svgElement = document.getElementById(country);
    if (svgElement) {
        svgElement.style.fill = "lightblue";
    }
  }

  let continentCount = continentCounts[continent]; // Get the count for the specific continent
  const maxCapacity = continentMaxCapacity[continent]; // Corrected continent names

  popupContent.textContent = `${continentCount}/${maxCapacity}`;
}

/*Main Popup */
function getPathClassName(event) {
  const path = event.target;
  const continent = path.getAttribute("class");
  const popup = document.getElementById(`${continent}-popup`);

  if (path.tagName === "path") {
      popup.style.display = "block";

      const popupWidth = popup.offsetWidth;
      const popupHeight = popup.offsetHeight;
      const mouseX = event.pageX;
      const mouseY = event.pageY;

      const popupX = mouseX - popupWidth / 2;
      const popupY = mouseY - popupHeight;

      popup.style.left = popupX + "px";
      popup.style.top = popupY + "px";

      const allPopups = document.querySelectorAll(".popup");
      allPopups.forEach(p => {
          if (p !== popup) {
              p.style.display = "none";
          }
      });

      popupkm(event);
  }
  
}


const svgPath = document.querySelectorAll("svg path");
svgPaths.forEach(path => {
  path.addEventListener("click", getPathClassName);
});

document.addEventListener("click", function(event) {
  if (!event.target.closest("path")) {
    const allPopups = document.querySelectorAll(".popup");
    allPopups.forEach(popup => {
      popup.style.display = "none";
    });
  }
});

const continentPopups = document.querySelectorAll(".popup");
continentPopups.forEach(popup => {
  popup.addEventListener("click", function(event) {
    event.stopPropagation();
  });
});

  




/*----------------------------------------------POPUP COUNTRIES JS JINIJA DICTIONARY----------- */

