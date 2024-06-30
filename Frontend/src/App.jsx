import React, { useState } from "react";

const App = () => {
  const [inputData, setInputData] = useState("");
  const handleSubmit = (e) => {
    e.preventDefault();
    //

    fetch("http://127.0.0.1:3000/create_ppt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(inputData),
    })
      .then((response) => console.log(response.json()))
      .catch((error) => console.error(error));
  };

  return (
    <>
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
    </>
  );
};

export default App;
