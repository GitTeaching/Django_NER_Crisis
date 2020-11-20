var file = document.getElementById('file');

file.onchange = function(e) {
  var ext = this.value.match(/\.([^\.]+)$/)[1];
  switch (ext) {
    case 'txt':
    case 'docx':
      break;
    default:
      alert('File format not allowed. Allowed extensions : .txt and .docx');
      this.value = '';
  }
};