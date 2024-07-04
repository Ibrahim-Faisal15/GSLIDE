import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Spinner from "react-bootstrap/Spinner";
import "./index.css";

const App = () => {
  const [inputData, setInputData] = useState("");
  const [loadState, setloadState] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    //

    setloadState(true);
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
        setloadState(false);
        const URL = window.URL.createObjectURL(blob);
        const link = document.createElement("a");

        link.href = URL;
        link.download = "file.pptx"; // Set default filename if not provided
        link.textContent = "Download File";
        document.body.appendChild(link);
        link.classList.add("hidden");
        link.click();
      })
      .catch((error) => {
        console.error("Error fetching or processing file2114:", error);
      });
  };

  return (
    <div>
      {/* Navbar */}
      <nav>
        <div className="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4">
          <a className="flex items-center space-x-3 rtl:space-x-reverse">
            <img src="../public/slides.svg" alt="Flowbite Logo" />
            <span className="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">
              GSlider
            </span>
          </a>
          <div className="flex items-center space-x-6 rtl:space-x-reverse ">
            <button
              type="button"
              className="  w-32 h-11   text-white   font-extrabold font-mono rounded-lg text-xl  px-4 py-2 text-center bg-[#3b3d40] hover:bg-[#222324]"
            >
              <a href="https://github.com/Ibrahim-Faisal15">GitHub</a>
            </button>
          </div>
        </div>
      </nav>

      <form
        onSubmit={handleSubmit}
        className="h-screen flex flex-col justify-center items-center "
      >
        <label className=" bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent text-5xl font-bold flex flex-col text-center mb-4 text ">
          <span className="mb-2">Generate your presentation</span>
          <span> in a productive manner.</span>
        </label>
        <input
          placeholder="Try Robot....."
          type="text"
          required
          value={inputData}
          onChange={(e) => setInputData(e.target.value)}
          className="w-[30vw]  h-12 rounded-lg pl-3 text-xl font-semibold font-mono border-4 border-[#1c1b1b] focus:outline-none"
        />
        {loadState ? (
          <Spinner
            animation="border"
            className="mb-52 relative top-14  h-24 w-24 text-white "
          />
        ) : (
          <button className="  mt-4 h-12 w-44 text-xl  text-white font-sans  bg-[conic-gradient(at_bottom_right,_var(--tw-gradient-stops))] from-blue-700 via-blue-800 to-gray-900 hover:bg-gradient-to-br  dark:focus:ring-cyan-800 font-medium rounded-lg  px-5 py-2.5 text-center me-2 mb-44">
            Generate
          </button>
        )}
      </form>
    </div>
  );
};

export default App;
