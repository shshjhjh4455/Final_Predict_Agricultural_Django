<<<<<<< HEAD
import React, { Component } from 'react';

class App extends Component {
  state = {
    accounts: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/user/signup');
      const accounts = await res.json();
      this.setState({
        accounts
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.accounts.map(item => (
          <div key={item.name}>
            <h1>{item.email}</h1>
            <span>{item.name}</span>
          </div>
        ))}
      </div>
=======
import {Route, Switch} from 'react-router-dom';
import React, {Suspense} from 'react';
import './App.css';
import NavBar from './components/NavBar/NavBar';	// 추가
import LoginPage from './components/UserPage/LoginPage';	// 추가
import SignupPage from './components/UserPage/SignupPage';	// 추가

function App() {
  return (
    <Suspense fallback={(<div>...</div>)}>
      <NavBar />
      <div className="App">
          <Switch>
            <Route exact path="/login" component={LoginPage}></Route>	
            <Route exact path="/signup" component={SignupPage}></Route>	
          </Switch>
        </div>
    </Suspense>
>>>>>>> parent of b674aa4a (update)
    );
  }
}

export default App;