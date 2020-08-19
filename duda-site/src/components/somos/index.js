import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'
import './somos.css'

import QuebraCabeca from '../../assets/img/quebra-cabeca.png'

//equipe
import andressa from '../../assets/img/andressa-min.png'
import juliana from '../../assets/img/juliana-min.png'
import yuri from '../../assets/img/yuri-min.png'
import max from '../../assets/img/max-min.png'
import vini from '../../assets/img/vini-min.png'
import ton from '../../assets/img/ton-min.png'

function Somos(){
    return(
        <Container fluid className="somos" id="somos">
            <Row>
                <Col xs={12} md={4} className="title-box" >
                    <img src={QuebraCabeca} alt="quem somos" />
                    <h2>QUEM SOMOS</h2>
                    <p>Uma galera gente boa e com skills complementares, disposta a inovar e a expandir a educação se reuniu para fundar o Educa²</p>
                </Col>
                <Col xs={12} md={8} className="equipe">
                    <Col xs={12} md={4}>
                        <img src={andressa}/>
                        <h3>ANDRESA OLIVEIRA</h3>
                        <p>EDUCAÇÃO</p>
                    </Col>
                    <Col xs={12} md={4}>
                        <img src={juliana}/>
                        <h3>JULIANA OLIVEIRA</h3>
                        <p>BUSINESS/PRODUTO</p>
                    </Col>
                    <Col xs={12} md={4}>
                        <img src={yuri}/>
                        <h3>YURI ABE</h3>
                        <p>PROJETOS</p>
                    </Col>
                    <Col xs={12} md={4}>
                        <img src={max} />
                        <h3>MAXWELL BORGES</h3>
                        <p>TECNOLOGIA</p>
                    </Col>
                    <Col xs={12} md={4}>
                        <img src={vini} />
                        <h3>VINICIO BREJINSKI</h3>
                        <p>TECNOLOGIA</p>
                    </Col>
                    <Col xs={12} md={4}>
                        <img src={ton} />
                        <h3>TON FREITAS</h3>
                        <p>UX DESIGNER</p>
                    </Col>
                </Col>
            </Row>
        </Container>
    )
}

export default Somos