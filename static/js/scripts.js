// Handle file drop event
function handleDrop(event) {
    event.preventDefault();
    const files = event.dataTransfer.files;
    if (files.length > 0) {
        handleFileSelect({target: {files}});  // Only handle one file for simplicity
    }
}

// Highlight drag-over state
function handleDragOver(event) {
    event.preventDefault();
    document.getElementById('upload-container').classList.add('dragover');
}

// Handle file selection (from drag or file input)
function handleFileSelect(event) {
    const fileInput = document.getElementById('fileInput');
    if (event.target && event.target.files.length > 0) {
        fileInput.files = event.target.files;
        console.log('File selected:', fileInput.files[0].name);  // Log selected file for debugging
    }
    document.getElementById('upload-container').classList.remove('dragover');
}

// Remove highlight when drag leaves the area
function handleDragLeave() {
    document.getElementById('upload-container').classList.remove('dragover');
}

// Trigger file input dialog when clicking inside the circle
function triggerFileInput() {
    document.getElementById('fileInput').click();
}
