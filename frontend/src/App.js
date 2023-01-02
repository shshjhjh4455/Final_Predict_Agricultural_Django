import React, { Suspense } from 'react';
import {Route, Routes} from "react-router-dom" ;
import "./App.css" ;
import NavBar from "./components/NavBar/NavBar" ;   // 추가
import LoginPage from './components/UserPage/LoginPage';	// 추가
import SignupPage from './components/UserPage/SignupPage';	// 추가


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

function App() {
  return (
    <Suspense fallback={(<div>...</div>)}>
      <NavBar />
      <div className="App">
          <Routes>
            <Route exact path="/login" element={LoginPage}></Route>	// 추가
            <Route exact path="/signup" element={SignupPage}></Route>	// 추가
          </Routes>
        </div>
    </Suspense>
    );
}

export default App;