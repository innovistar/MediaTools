const dropArea = document.querySelector(".drop_box"),
  button = dropArea.querySelector("button"),
  dragText = dropArea.querySelector("header"),
  input = dropArea.querySelector("input");
let file;
var filename;

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function (e) {
  var fileName = e.target.files[0].name;
  let filedata = `
    <div class="form">
    <h4>${fileName}</h4>
    
    </div>`;
  dropArea.innerHTML = filedata;
});
