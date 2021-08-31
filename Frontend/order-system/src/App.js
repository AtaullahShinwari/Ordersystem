import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import './App.css';
import Home from './components/Home'
import Speisen from './components/Speisen'
import Submenu from './components/Submenu'
import Tst from './components/test'

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Tst}/>
        <Route path="/Submenu" exact component={Submenu}/>
        <Route path="/Speisen" exact component={Speisen}/>
      </Switch>
    </Router>
  );
}

export default App;
