import React, { Component } from 'react';
import {Route, routes} from 'react-router-dom';
import NavBar from './components/NavBar/NavBar';	// 추가
import LoginPage from './components/UserPage/LoginPage';	// 추가
import SignupPage from './components/UserPage/SignupPage';	// 추가

function App() {
    return (
      <Suspense fallback={(<div>...</div>)}>
        <NavBar />
        <div className="App">
            <routes>
              <Route exact path="/login" element={LoginPage}></Route>	
              <Route exact path="/signup" element={SignupPage}></Route>	
            </routes>
          </div>
      </Suspense>
      );
  }
  
  export default App;

// class App extends Component {
//   state = {
//     accounts: []
//   };

//   async componentDidMount() {
//     try {
//       const res = await fetch('http://127.0.0.1:8000/user/login/1/');
//       const accounts = await res.json();
//       this.setState({
//         accounts
//       });
//     } catch (e) {
//       console.log(e);
//     }
//   }

//   render() {
//     return (
//       <div>
//         {this.state.accounts.map(item => (
//           <div key={item.name}>
//             <h1>{item.email}</h1>
//             <span>{item.name}</span>
//           </div>
//         ))}
//       </div>
//     );
//   }
// }

// export default App;