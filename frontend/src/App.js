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
    );
}

export default App;