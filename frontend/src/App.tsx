import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { LandingPage } from './pages/LandingPage';
import { JornadaPage } from './pages/JornadaPage';
import { AdminPage } from './pages/AdminPage';
import { InsightsPage } from './pages/InsightsPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/jornada" element={<JornadaPage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/insights" element={<InsightsPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
