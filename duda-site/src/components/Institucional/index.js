import React from 'react'
import { Container, Row, Col, Carousel} from 'react-bootstrap'
import './inst.css'

//import img
import iconMissao from '../../assets/img/missao.png'
import iconVisao from '../../assets/img/visao.png'
import iconValores from '../../assets/img/valores.png'

//impor img slid
import missao from '../../assets/img/missao-slid.png'
import visao from '../../assets/img/visao-slid.png'
import valores from '../../assets/img/valores-slid.png'


function Institucional(){
    return(
        <Container fluid className="institucional" id="institucional">

            <Row className="d-md-none">
                <Carousel className="slid-container">
                    <Carousel.Item>
                        <img
                        className="d-block w-100"
                        src={missao}
                        alt="Missão"
                        />
                        <Carousel.Caption>
                        <h3>MISSÃO</h3>
                        <p className="text-slid" >Nosso propósito é tornar o ensino democrático, acessível e gratuito para todo e qualquer aluno.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                        className="d-block w-100"
                        src={visao}
                        alt="Missão"
                        />
                        <Carousel.Caption>
                        <h3>VISÃO</h3>
                        <p className="text-slid" >Nos tornar reconhecidos por alcançar de maneira eficiente aqueles que são excluídos digital.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                        className="d-block w-100"
                        src={valores}
                        alt="Missão"
                        />
                        <Carousel.Caption>
                        <h3>VALORES</h3>
                        <p className="text-slid" >Inovação da metodologia de ensino, cooperação, tranformação social através da educação.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                </Carousel>

            </Row>

            <Row className="d-none d-md-flex mt-5 icons-line">
                <Col md="3" className="icons-container" >
                    <h3 className="inst-title" >MISSÃO</h3>
                    <img  className="inst-icon" src={iconMissao} alt="missão" />
                    <p className="inst-text">Nosso propósito é tornar o ensino democrático, acessível e gratuito para todo e qualquer aluno.</p>
                </Col >
                <Col md="3" className="icons-container">
                    <h3 className="inst-title" >VISÃO</h3>
                    <img  className="inst-icon" src={iconVisao} alt='visão' />
                    <p className="inst-text">Nos tornar reconhecidos por alcançar de maneira eficiente aqueles que são excluídos digital.</p>
                </Col>
                <Col md="3" className="icons-container">
                    <h3 className="inst-title" >VALORES</h3>
                    <img  className="inst-icon" src={iconValores} alt='valores' />
                    <p className="inst-text">Inovação da metodologia de ensino, cooperação, tranformação social através da educação.</p>
                </Col>
            </Row>
            
        </Container>
    )
}

export default Institucional