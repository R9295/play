import React from 'react';
import ReactDOM from 'react-dom';
import { Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button, Row, Col } from 'reactstrap';

class Players extends React.Component {
  render () {
    let players = window.props;
    console.log(window.props)
    return <Row>{players.map(item => <Player key={item.id}
                        personaname={item.personaname}/> )}</Row>;
  }
}

class Player extends React.Component {
  render() {
    return  (
      <Col md="12" lg="12" sm="12">
       <Card>
         <CardBody>
           <CardTitle>{ this.props.personaname }</CardTitle>
           <CardSubtitle>Card subtitle</CardSubtitle>
           <CardText>"Some quick example text to build on the card title and make up the bulk of the card's content"</CardText>
           <Button>Button</Button>
         </CardBody>
       </Card>
     </Col>
   )
    }
}

ReactDOM.render(
  <Players />,
  document.getElementById('players')
)
