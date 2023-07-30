const kidsInput = document.getElementById("kidsInput");
const kidsForm = document.getElementById("kidsForm");

kidsInput.addEventListener("input", function () {
  const kidsCount = parseInt(kidsInput.value);

  if (kidsCount >= 1) {
    kidsForm.classList.remove("hidden");
  } else {
    kidsForm.classList.add("hidden");
  }
});

const spouseInput = document.getElementById("spouseInput")
const spouseForm = document.getElementById("spouseForm")
// const inputSpouse = document.getElementById("spouseInput");

spouseInput.addEventListener("input", function () {
const selectedValue = spouseInput.value.toLowerCase().trim();
  if (selectedValue === 'married') {
    spouseForm.classList.remove("hidden");
  } else {
    spouseForm.classList.add("hidden")
  }
})

