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

function getPathClassName(event) {
    const path = event.target;
    const continent = path.getAttribute("class");
    const popup = document.getElementById(`${continent}-fraction`);

}
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

const popupContent = document.getElementById(`${continent}-fraction`);

  
let countries = {
  "USA": "North America",
  "France": "Europe",
  "China": "Asia",
  "Brazil": "South America",
};

let europeCount = 0;
let asiaCount = 0;
let northAmericaCount = 0;
let southAmericaCount = 0;
let oceaniaCount = 0;
let afrikaCount = 0;

for (let country in countries) {
  let continent = countries[country];

  switch (continent) {
      case "Europe":
          europeCount++;
          break;
      case "Asia":
          asiaCount++;
          break;
      case "North America":
          northAmericaCount++;
          break;
      case "South America":
          southAmericaCount++;
          break;
      case "Oceania":
          oceaniaCount++;
          break;
      case "Africa":
          africaCount++;
          break;
  }
}
const continentMaxCapacity = {
  "Europe": 44,
  "Asia": 49,
  "North-America": 23,
  "South-America": 12,
  "Africa": 54,
  "Oceania": 12
};

popupContent.innerHTML = "213231/322421";




/*----------------------------------------------POPUP COUNTRIES JS JINIJA DICTIONARY----------- */

for (let country in countries) {
  let continent = countries[country];

  let svgElement = document.getElementById(country);
  if (svgElement) {
      svgElement.style.fill = "lightblue";
  }
}