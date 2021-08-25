import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import './App.css';
import Home from './components/Home'
import Speisen from './components/Speisen'
import Submenu from './components/Submenu'

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home}/>
        <Route path="/Submenu" exact component={Submenu}/>
        <Route path="/Products" exact component={Speisen}/>
      </Switch>
    </Router>
  );
}

export default App;
