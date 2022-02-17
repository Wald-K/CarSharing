import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';
import CarList from "./components/CarList";
import CarDetail from "./components/CarDetail"

function App() {
  return (
    <div className="App">
      <BrowserRouter>    
        <Routes>    
          <Route exact path="cars" element={<CarList/>} />
          <Route exact path="cars/:id" element={<CarDetail />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
