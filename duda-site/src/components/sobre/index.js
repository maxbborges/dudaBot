import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'
import './sobre.css'

import torre from '../../assets/img/torre.png'
import setaRight from '../../assets/img/seta-right.png'
import setaDown from '../../assets/img/seta-down.png'
import pessoas from '../../assets/img/pessoas.png'

function Sobre(){
    return(
        <Container fluid className="sobre" id="sobre" >
            <Row>
                <Col>
                    <h3>O QUE É<br/> O EDUCA²</h3>
                </Col>
            </Row>
            <Row>
                <Col xs={12} lg={{ span: 4, offset: 1 }} offset={1} className="torre-container" >
                    <img src={torre} alt="Torre icon" className="torre" />
                    <p className="text-torre">O Educa² é o sistema de transmissão instantânea de áudio aulas via sinal de telefone</p>
                </Col>
                <Col xs={12} lg={2} className="seta-container" >
                    <img src={(window.innerWidth > 992)?setaRight:setaDown} alt="seta" className="seta" />
                </Col>
                <Col xs={12} lg={4} className="pessoas-container" >
                    <img src={pessoas} alt="pessoas" className="pessoas" />
                    <p className="text-pessoas" >Conectando de forma simples e barata professores e alunos</p>
                </Col>
            </Row>
        </Container>
    )
}

export default Sobre