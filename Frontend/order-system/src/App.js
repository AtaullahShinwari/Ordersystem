import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import './App.css';
import Home from './components/Home'
import Products from './components/Products'

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home}/>
        <Route path="/Products" exact component={Products}/>
      </Switch>
    </Router>
  );
}

export default App;
