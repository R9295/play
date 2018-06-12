import React from 'react'
import ReactDOM from 'react-dom'
import { Button, Form, FormGroup, Label, Input, FormText, Col, Alert } from 'reactstrap';

//import 'bootstrap/dist/css/bootstrap.css';
class ProfileForm extends React.Component {

  constructor(props){
    super(props);
    this.state = {update: false, loading: true,status: null, response:[], selected: {}}
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  async getOptions(){
    let heroes = await fetch('/api/v1/heroes')
    heroes = await heroes.json()

    let servers = await fetch('/api/v1/servers')
    servers = await servers.json()

    let roles = await fetch('/api/v1/roles')
    roles = await roles.json()

    // get old profile if exists
    let profile = await fetch('/api/v1/users/'+window.props.user)
    profile = await profile.json()
    profile = profile.profile
    if (profile != null){
      this.setState({
        selected: {
          servers: profile.fav_servers,
          heroes: profile.fav_heroes,
          roles: profile.fav_roles,
        },
        update: true,
        // set profile_pk if there is a profile so that the url can be built to update.
        profile_pk: profile.id
      })
    }
    this.setState({
      roles: roles,
      servers: servers,
      heroes: heroes,
      loading: false,
    })
    document.getElementById('response').style.visibility = "hidden";
  }
  componentWillMount(){
    this.getOptions()
  }
  async handleSubmit(event){
    event.preventDefault();
    let form_data = new FormData(event.target);
    let data = {
      user: window.props.user,
      profile:{
        csrf_token: form_data.getAll('csrf_token'),
        fav_roles: form_data.getAll('fav_roles'),
        fav_servers: form_data.getAll('fav_servers'),
        fav_heroes: form_data.getAll('fav_heroes'),
      }
    }
    data = JSON.stringify(data)
    // construct url to either update or create instance
    const url = '/api/v1/users/'+window.props.user+'/profile/'
    const method = 'POST'
    let response = await fetch(url,{
      method: method,
      body: data,
      headers: {
        'X-CSRFToken': window.props.csrf_token,
        'Content-Type': 'application/json'
      }
    })
    let json = await response.json()
    console.log(json)
    // if serializer returns an error
    if (response.status === 400){
  //    console.log(response.status)
      this.handleErrors(json)
    }
    // if success
    if (response.status === 201 || response.status === 200) {
      if (!this.state.update){
        // if it was a new instance, getOptions to update to new values
        // and set state to update.
        this.getOptions()
      }
      this.handleSuccess(json)
    }
  }
  handleErrors(errors){
    // clear response first
    this.setState({
        response: [],
        status: "error",
    })
    // append all errors
    Object.keys(errors.profile).forEach(key => this.setState(
      {
        response: [...this.state.response, errors.profile[key][0]]
      }
    ))
    document.getElementById('response').style.visibility = "visible";
  }
  handleSuccess(success){
    this.setState({
        response: this.state.update ? ['Successfully updated your profile'] : ['Successfully created your profile'],
        status: "success",
    })
    document.getElementById('response').style.visibility = "visible";
  }
  render () {
    //{this.state.response.forEach(item => <h6>{ item }</h6>)}
      //this.state.response.forEach(item => console.log(item))
      if (this.state.loading){
        return  <h1> LOADING </h1>
      } else {
        return (
          <div>
            <div id="response">
              <Alert color={this.state.status=="success" ? 'success':'danger'}>{ this.state.response.map(item => <h6 key={item}>{item}</h6>)}</Alert>
            </div>
          <Form onSubmit={this.handleSubmit} id="form" encType="multipart/form-data">
          <Col sm="6" lg="6" md="6">
          <Input type="hidden" name="user" value={window.props.user} />
          <FormGroup>
            <Label for="fav_servers">Preferred Servers</Label>
            <Input type="select" name="fav_servers" id="fav_servers" multiple defaultValue={this.state.selected.servers}>
            {this.state.servers.map(item => <Option key={item.name} name={ item.name } /> )}
            </Input>
            </FormGroup>

          <FormGroup>
            <Label for="fav_heroes">Preferred Heroes</Label>
            <Input type="select" name="fav_heroes" id="fav_heroes" multiple defaultValue={this.state.selected.heroes}>
            {this.state.heroes.map(item => <Option key={item.name} name={ item.name }/> )}
            </Input>
          </FormGroup>

          <FormGroup>
            <Label for="fav_roles">Preferred Roles</Label>
            <Input type="select" name="fav_roles" id="fav_roles" multiple defaultValue={this.state.selected.roles}>
            {this.state.roles.map(item => <Option key={item.name} name={ item.name }/> )}
            </Input>
          </FormGroup>

          </Col>
          <Button> Save </Button>
          </Form>
          </div>
        )
    }
  }
}

class Option extends React.Component {
  render () {
    return (
      <option value={ this.props.name } key={ this.props.name }>{ this.props.name }</option>
    )
  }
}

ReactDOM.render(
  <ProfileForm />,
  document.getElementById('form')
);
