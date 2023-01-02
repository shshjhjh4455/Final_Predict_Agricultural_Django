import {Route} from 'react-router-dom';
import React, {Suspense} from 'react';
import './App.css';
import NavBar from './elements/NavBar/NavBar';	// 추가
import LoginPage from './elements/UserPage/LoginPage';	// 추가
import SignupPage from './elements/UserPage/SignupPage';	// 추가

function App() {
  return (
    <Suspense fallback={(<div>...</div>)}>
      <NavBar />
      <div className="App">
          <Route>
            <Route exact path="/login" element={LoginPage}></Route>	
            <Route exact path="/signup" element={SignupPage}></Route>	
          </Route>
        </div>
    </Suspense>
    );
}

export default App;

