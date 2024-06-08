<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Word Puncher Test Client</title>
</head>
<body>
    <h1>Word Puncher GUI (for Testing Only)</h1>
    <form action="/upload-file" method="post">
        <label for="file">Upload a text file (currently supported docx and txt):</label>
        <br>
        <input type="file" id="text-file-upload" name="text-file" accept=".txt, .doc, .docx" />
        <br>
        <button type="submit">Upload File</button>
    </form>
    <div>
        <h2>Output</h2>
        <div id="output" style="height: 568px; width: 368px; border: 1px solid black;">
            {{ output }}
        </div>
    </div>
    <script src="assets/app.js"></script>
</body>
</html>