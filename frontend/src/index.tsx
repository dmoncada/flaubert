import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import ContentsRoute from "./routes/ContentsRoute";
import EntryRoute from "./routes/EntryRoute";

import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<>Dictionnaire des idées reçues</>}></Route>
        <Route path="/entries">
          <Route path="" element={<ContentsRoute />} />
          <Route path=":key" element={<EntryRoute />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
