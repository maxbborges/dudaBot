import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import Termos from './screens/termos';
import notfound from './screens/erros'
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter,Switch, Route } from 'react-router-dom'


ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path="/" exact={true} component={App} />
      <Route path="/termos" component={Termos} />
      <Route path='*' component={notfound} />
    </Switch>
  </ BrowserRouter>
  , document.getElementById('root')
  // <React.StrictMode>
  //   <App />
  // </React.StrictMode>,
  // document.getElementById('root')
);