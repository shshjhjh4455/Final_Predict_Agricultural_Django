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
    );
  }
}

export default App;