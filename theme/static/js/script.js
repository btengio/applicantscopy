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

const spouseInput = document.querySelector("spouseInput")
const spouseForm = document.getElementById("spouseForm")

spouseInput.addEventListener("change", function () {
  const inputSpouse = document.querySelector("spouseInput");
  if (inputSpouse === 'Married') {
    spouseForm.classList.remove("hidden");
  } else {
    spouseForm.classList.add("hidden")
  }
})

  