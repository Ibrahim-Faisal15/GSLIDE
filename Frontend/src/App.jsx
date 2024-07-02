import "../src/App.css";
import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  const [inputData, setInputData] = useState("");
  const handleSubmit = (e) => {
    e.preventDefault();
    //

    fetch("http://127.0.0.1:5000/create_ppt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(inputData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const blob = response.blob();
        return blob;
      })
      .then((blob) => {
        const URL = window.URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = URL;
        link.download = "file.pptx"; // Set default filename if not provided
        link.textContent = "Download File";
        document.body.appendChild(link);
      })
      .catch((error) => {
        console.error("Error fetching or processing file2114:", error);
      });
  };

  return (
    <center>
      <div class="input-group input-group-md mb-3">
        <input
          type="text"
          class="form-control"
          aria-label="Sizing example input"
          aria-describedby="inputGroup-sizing-md"
        ></input>
      </div>
      <form onSubmit={handleSubmit}>
        <label>Input Data</label>
        <input
          type="text"
          required
          value={inputData}
          onChange={(e) => setInputData(e.target.value)}
        />
        <br />
        <button>Generate</button>
      </form>
    </center>
  );
};

export default App;
