var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form ...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  // ... and run a function that displays the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form... :
  if (currentTab >= x.length) {
    //...the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false:
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class to the current step:
  x[n].className += " active";
}

const displayWeight = document.getElementById('display-weight')
const weightValue = document.getElementById('dog-weight')

weightValue.addEventListener('change', (e) => {
  const newWeight = e.currentTarget.value
  displayWeight.innerHTML = `Dog's current weight: ${newWeight}LBS`
});



const breeds = ["Affenpinscher", "Afghan Hound", "African Hunting Dog", "Airedale Terrier", "Akbash Dog", "Akita", "Alapaha Blue Blood Bulldog", "Alaskan Husky", "Alaskan Malamute", "American Bulldog", "American Bully", "American Eskimo Dog", "American Eskimo Dog (Miniature)", "American Foxhound", "American Pit Bull Terrier", "American Staffordshire Terrier", "American Water Spaniel", "Anatolian Shepherd Dog", "Appenzeller Sennenhund", "Australian Cattle Dog", "Australian Kelpie", "Australian Shepherd", "Australian Terrier", "Azawakh", "Barbet", "Basenji", "Basset Bleu de Gascogne", "Basset Hound", "Beagle", "Bearded Collie", "Beauceron", "Bedlington Terrier", "Belgian Malinois", "Belgian Tervuren", "Bernese Mountain Dog", "Bichon Frise", "Black and Tan Coonhound", "Bloodhound", "Bluetick Coonhound", "Boerboel", "Border Collie", "Border Terrier", "Boston Terrier", "Bouvier des Flandres", "Boxer", "Boykin Spaniel", "Bracco Italiano", "Briard", "Brittany", "Bull Terrier", "Bull Terrier (Miniature)", "Bullmastiff", "Cairn Terrier", "Cane Corso", "Cardigan Welsh Corgi", "Catahoula Leopard Dog", "Caucasian Shepherd (Ovcharka)", "Cavalier King Charles Spaniel", "Chesapeake Bay Retriever", "Chinese Crested", "Chinese Shar-Pei", "Chinook", "Chow Chow", "Clumber Spaniel", "Cocker Spaniel", "Cocker Spaniel (American)", "Coton de Tulear", "Dalmatian", "Doberman Pinscher", "Dogo Argentino", "Dutch Shepherd", "English Setter", "English Shepherd", "English Springer Spaniel", "English Toy Spaniel", "English Toy Terrier", "Eurasier", "Field Spaniel", "Finnish Lapphund", "Finnish Spitz", "French Bulldog", "German Pinscher", "German Shepherd Dog", "German Shorthaired Pointer", "Giant Schnauzer", "Glen of Imaal Terrier", "Golden Retriever", "Gordon Setter", "Great Dane", "Great Pyrenees", "Greyhound", "Griffon Bruxellois", "Harrier", "Havanese", "Irish Setter", "Irish Terrier", "Irish Wolfhound", "Italian Greyhound", "Japanese Chin", "Japanese Spitz", "Keeshond", "Komondor", "Kooikerhondje", "Kuvasz", "Labrador Retriever", "Lagotto Romagnolo", "Lancashire Heeler", "Leonberger", "Lhasa Apso", "Maltese", "Miniature American Shepherd", "Miniature Pinscher", "Miniature Schnauzer", "Newfoundland", "Norfolk Terrier", "Norwich Terrier", "Nova Scotia Duck Tolling Retriever", "Old English Sheepdog", "Olde English Bulldogge", "Papillon", "Pekingese", "Pembroke Welsh Corgi", "Perro de Presa Canario", "Pharaoh Hound", "Plott", "Pomeranian", "Poodle (Miniature)", "Poodle (Toy)", "Pug", "Puli", "Pumi", "Rat Terrier", "Redbone Coonhound", "Rhodesian Ridgeback", "Rottweiler", "Russian Toy", "Saint Bernard", "Saluki", "Samoyed", "Schipperke", "Scottish Deerhound", "Scottish Terrier", "Shetland Sheepdog", "Shiba Inu", "Shih Tzu", "Shiloh Shepherd", "Siberian Husky", "Silky Terrier", "Smooth Fox Terrier", "Soft Coated Wheaten Terrier", "Spanish Water Dog", "Spinone Italiano", "Staffordshire Bull Terrier", "Standard Schnauzer", "Swedish Vallhund", "Thai Ridgeback", "Tibetan Mastiff", "Tibetan Spaniel", "Tibetan Terrier", "Toy Fox Terrier", "Treeing Walker Coonhound", "Vizsla", "Weimaraner", "Welsh Springer Spaniel", "West Highland White Terrier", "Whippet", "White Shepherd", "Wire Fox Terrier", "Wirehaired Pointing Griffon", "Wirehaired Vizsla", "Xoloitzcuintli", "Yorkshire Terrier"]


//on load of certain element
const breedOptions = document.getElementById('breed-options')

  breeds.forEach((breed, i) => {
    console.log('breed', breed)

    let newOption = document.createElement('option')
    newOption.innerHTML = breed
    newOption.setAttribute('value', i+1)
    console.log(newOption)
    breedOptions.append(newOption)
  })
