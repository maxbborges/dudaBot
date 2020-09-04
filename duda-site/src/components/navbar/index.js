import React from 'react'
import { Nav, Navbar} from 'react-bootstrap'
import './navbar.css'


import EducaIcon from '../../assets/icons/educa.png'

function MainNavbar(){
    return(
        <Navbar expand="lg" className="bg-navbar">
            <Navbar.Brand href="/#banner" className="logo" ><img className="img-icon-educa" src={EducaIcon} alt='Educa²' /><span className="text-white">EDUCA²</span></Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="/#sobre" ><span className="nav-link-opt" >SOBRE O EDUCA</span></Nav.Link>
                    <Nav.Link href="/#institucional" ><span className="nav-link-opt" >INSTITUCIONAL</span></Nav.Link>
                    <Nav.Link href="/#funciona" ><span className="nav-link-opt" >COMO FUNCIONA</span></Nav.Link>
                    <Nav.Link href="/#surgiu" ><span className="nav-link-opt" >COMO SURGIU</span></Nav.Link>
                    <Nav.Link href="/#somos" ><span className="nav-link-opt" >QUEM SOMOS</span></Nav.Link>
                    <Nav.Link href="/termos" ><span className="nav-link-opt" >TERMOS E POLÍTICA</span></Nav.Link>
                </Nav>    
            </Navbar.Collapse>
        </Navbar>
    )
}

export default MainNavbar