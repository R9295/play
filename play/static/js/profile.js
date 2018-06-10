import React from 'react'
import ReactDOM from 'react-dom'
import { Button, Form, FormGroup, Label, Input, FormText, Col, Alert } from 'reactstrap';

//import 'bootstrap/dist/css/bootstrap.css';
class ProfileForm extends React.Component {

  constructor(props){
    super(props);
    this.state = {error: '', success: false, loading: true, errors:[], selected: {}}
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
    let profile = await fetch('/api/v1/users/'+window.props.user+'/profile')
    profile = await profile.json()
    if (!profile.error){
      this.setState({
        selected: {
          servers: profile.fav_servers,
          heroes: profile.fav_heroes,
          roles: profile.fav_roles,
        }
      })
    }
    this.setState({
      roles: roles,
      servers: servers,
      heroes: heroes,
      loading: false,
    })
  }


  componentWillMount(){
    this.getOptions()
  }
  async handleSubmit(event){
    event.preventDefault();
    let data = new FormData(event.target);
    let response = await fetch('/api/v1/profile/',{
      method: 'POST',
      body: data
    })
    let json = await response.json()
    if (response.status == 400){
      // if serializer error
      this.handleErrors(json)
    }
    if (response.status == 201) {
      // if successs
      this.handleSuccess(json)
    }
  }
  handleErrors(errors){
    document.getElementById('response').removeAttribute("hidden")
  }
  handleSuccess(success){
    console.log(success)
  }
  render () {
      if (this.state.loading){
        return  <h1> LOADING </h1>
      } else {
        return (
          <Form onSubmit={this.handleSubmit}>
          <Alert color="danger" hidden id="response">  { this.state.errors }</Alert>
          <Col sm="6" lg="6" md="6">
          <Input type="hidden" name="user" value={window.props.user} />
          <Input type="hidden" name="csrfmiddlewaretoken" value={window.props.csrf_token} />

          <FormGroup>
            <Label for="fav_servers">Preferred Servers</Label>
            <Input type="select" name="fav_servers" id="fav_servers" multiple defaultValue={this.state.selected.servers}>
            {this.state.servers.map(item => <Option key={ item.id } id={ item.id } name={ item.name } /> )}
            </Input>
            </FormGroup>

          <FormGroup>
            <Label for="fav_heroes">Preferred Heroes</Label>
            <Input type="select" name="fav_heroes" id="fav_heroes" multiple>
            {this.state.heroes.map(item => <Option key={ item.id } id={ item.id } name={ item.name }/> )}
            </Input>
          </FormGroup>

          <FormGroup>
            <Label for="fav_roles">Preferred Roles</Label>
            <Input type="select" name="fav_roles" id="fav_roles" multiple>
            {this.state.roles.map(item => <Option  key={ item.id } id={ item.id } name={ item.name }/> )}
            </Input>
          </FormGroup>

          </Col>
          <Button> Save </Button>
          </Form>
        )
    }
  }
}

class Option extends React.Component {
  render () {
    return (
      <option value={ this.props.id } key={this.props.id}>{ this.props.name }</option>
    )
  }
}
ReactDOM.render(
  <ProfileForm />,
  document.getElementById('form')
);
