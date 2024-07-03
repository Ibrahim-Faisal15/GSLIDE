import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";

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
    <div>
      <form
        onSubmit={handleSubmit}
        className="h-screen flex flex-col justify-center items-center"
      >
        {/* <label className="text-sky-400/100">Input Data</label> */}
        <input
          type="text"
          required
          value={inputData}
          onChange={(e) => setInputData(e.target.value)}
          className="w-80"
        />

        <button className="text-red-200">Generate</button>
      </form>
    </div>
  );
};

export default App;
