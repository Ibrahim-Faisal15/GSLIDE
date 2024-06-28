import React from "react";

const App = () => {
  return (
    <>
      <form action="http://127.0.0.1:5000/create_ppt">
        <label>Input Data</label>
        <input type="text" required />
        <br />
        <button>Generate</button>
      </form>
    </>
  );
};

export default App;
