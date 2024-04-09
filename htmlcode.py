# Código de apoio à construção da página index.html do sítio cfaeca.pt
# Deve ser considerado eventua alteração à string
# Nota importante usar triplo quotes na definição das strings, de inicio e final (não deixar que o compilador altere
# texto.py
# Defina uma variável com o texto desejado
from datetime import datetime

# Obter a data e hora atual no formato YYYY-MM-DD HH:MM
data_atualizacao = datetime.now().strftime('%Y-%m-%d %H:%M')
# HTML para a linha adicional com a data de atualização
linha_data_atualizacao: str = f'<li style="font-size: 12px;">Data de criação - 2023-11-01 | Data de atualização - {data_atualizacao}</li>'

print( {linha_data_atualizacao})
str_html_init = '''
<!DOCTYPE html>
<html lang="pt-PT">
<head>
	<title>Centro de Formação CFAECA</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="css/all.css">
	<link rel="stylesheet" type="text/css" href="css/all.min.css">
	<link rel="stylesheet" type="text/css" href="css/lightbox.css">
	<link rel="stylesheet" type="text/css" href="css/flexslider.css">
	<link rel="stylesheet" type="text/css" href="css/owl.carousel.css">
	<link rel="stylesheet" type="text/css" href="css/owl.theme.default.css">
	<link rel="stylesheet" type="text/css" href="css/jquery.rateyo.css"/>
	<link rel="stylesheet" type="text/css" href="css/jquery.mmenu.all.css"/> 
	<link rel="stylesheet" type="text/css" href="css/meanmenu.min.css">
	<link rel="stylesheet" type="text/css" href="inner-page-style.css">
	<link rel="stylesheet" type="text/css" href="style.css">
	<link href="https://fonts.googleapis.com/css?family=Raleway:400,500,600,700" rel="stylesheet">
	<link rel="shortcut icon" type="imagex/png" href="./images/icon.ico">
	
	<style>
        @keyframes blink {
            0% { color: green; }
            50% { color: white; }
            100% { color: green; }
        }
        
        .flashing-text {
            animation: blink 2s infinite;
        }
    </style>
</head>
<body>
	<div id="page" class="site" itemscope itemtype="http://schema.org/LocalBusiness">
		<header class="site-header">
				
			<div class="main-header">
				<div class="container">
					<div class="logo-wrap" itemprop="logo">
						<img src="images/logocfaeca.png" alt="Logo Imagem CFAECA"  style="width: 60%; height: auto; float: left; margin-right: 2px; margin-top: -5px">
					</div>
						 <h2 style="clear: both;">
							 <ul>			
							 <li><a href="https://www.office.com/"> <img src="images/acesso365.png" alt="Office 365 Logo" style="width: 50%; height: auto; float: left;margin-right: 10px;margin-top: -5px;"></a></li>
							   <li><a href="https://moodle2020.cfaeca.org/"> <img src="images/Moodle-logo.png" alt="Moodle Logo" style="width: 40%; height: auto;float: left; "></a></li>
						      </ul>
					    </h2>
					</div>
			</div>
		</header>
		<!-- Top header Close -->
			<div class="main-header">
				<div class="container" style="margin-top: -50px">
					
					<div class="nav-wrap">
						<nav class="nav-desktop">
							<ul class="menu-list">
								<li><a href="noticias.html">Notícias</a></li>
								<li class="menu-parent">Formação
									<ul class="sub-menu">
										
										<li><a href="#formacaocurso">Aceita inscrições</a></li>
										<li><a href="./docs/lista_acoes_candidatura_pf2023.pdf">Ações realizadas</a></li>
										<li><a href="https://forms.gle/MBsbLtkzM23k1TYN6">Atualização dados Plataformas CFAECA</a></li>
														
									</ul>
								</li>
								
								<li class="menu-parent">Avaliação
									<ul class="sub-menu">
									<li class="menu-parent">ADD
											<ul class="sub-menu">
											   <a href="https://diariodarepublica.pt/dr/detalhe/despacho-normativo/24-2012-3293885">ADD - Coordenação Bolsa Avaliadores</a></li>
											   <li><a href="https://www.dgae.medu.pt/institucional/notas-informativas">ADD - Notas informativas</a></li>
												<li><a href="https://dre.tretas.org/dre/304414/despacho-13981-2012-de-26-de-outubro">ADD - Avaliação externa</a></li>
												<li><a href="https://files.diariodarepublica.pt/1s/2012/08/16800/0491204916.pdf">ADD - Diretores</a></li>
												<li><a href="https://files.diariodarepublica.pt/1s/2012/02/03700/0085500861.pdf">Regime Geral ADD</a></li>
												<li><a href="https://files.diariodarepublica.pt/1s/2012/02/03700/0082900855.pdf">Estatuto Carreira Docente</a></li>
											</ul>
										</li>
										
							</li>
										
										<li><a href="./docs/REQUERIMENTO_OBSERVACAO_DE_ESCOLAS.xlsx" title="editável - apenas são aceites documentos preenchidos através de editores folha de cálculo - p.ex. Excel">
                                 Requerimento observação aulas </a></li>
																										
										<li><a href="https://www.dgae.medu.pt/gestrechumanos/pessoal-docente/carreira/avaliacao-do-desempenho#docentes" ">
                                 SIADAP </a></li>
				
									</ul>
														
								</li>
	
								<li class="menu-parent"> Projetos
									<ul class="sub-menu">
										<li><a href="http://www.ie.ulisboa.pt/geral/ie-ulisboa-nova-colaboracao-com-c-m-amadora">Escolas@Digitais</a></li>
										<li><a href="https://escxel.com/">ESCXEL</a></li>
										<li><a href="https://erasmusmais.pt/erasmus/programa/">Erasmus+</a></li>
										<li><a href="https://www.pisaparaasescolas.pt/">PISA PARA AS ESCOLAs</a></li>
										<li><a href="./docs/PROJETO_SEMEIA_Amadora.pdf">SEMEIA</a></li>
										
									</ul>
								</li>
								
								<li class="menu-parent"> Recursos
									<ul class="sub-menu">
										<li><a href="https://moodle2020.cfaeca.org/login/index.php	">Plataforma Moodle</a></li>
										<li><a href="https://www.office.com/">Plataforma M365Edu</a></li>
																				
									</ul>
								</li>
								
							<li class="menu-parent"> Institucional
									<ul class="sub-menu">
									   <li><a href="https://www.dgae.medu.pt/">DGAE</a></li>
										<li><a href="https://www.dge.mec.pt/autonomia-e-flexibilidade-curricular">Autonomia Flexibilidade Curricular</a></li>
										<li><a href="https://digital.dge.mec.pt/">Capacitação Digital</a></li>
										<li><a href="https://infoescolas.medu.pt/3Ciclo/">INFO-ESCOLAS</a></li>
										<li><a href="https://iave.pt/">IAVE</a></li>															
									</ul>
								</li>										
								<li><a href="./docs/direcaop.pdf">Direção</a></li>
								
								<li class="menu-parent"> Legal
									<ul class="sub-menu">
										<li><a href="#">Legislação contextual</a></li>
										<li><a href="./docs/RI_CFAECA.pdf">Regulamento Interno</a></li>
									</ul>
								</li>						
							<li><a href="#contacto">Contactos</a></li>
							</ul>
						</nav>
						<div id="bar">
							<i class="fas fa-bars"></i>
						</div>
						<div id="close">
							<i class="fas fa-times"></i>
						</div>
					</div>
				</div>
			</div>
		<div class="banner"  style="margin-botton: 10px;">
			<div class="owl-four owl-carousel" itemprop="image">
				<img src="images/page-banner.jpg" alt="Imagem número 1 do Bannner">
				<img src="images/page-banner2.jpg" alt="Imagem número 2 do Bannner">
				<img src="images/page-banner3.jpg" alt="Imagem número 3  do Bannner">
				<img src="images/page-banner4.jpg" alt="Imagem número 4 do Bannner">
			</div>
			<div class="container" itemprop="description">
				
				<h1>Centro de Formação da Associação de Escolas do Concelho da Amadora</h1>
			</div>
			 <div id="owl-four-nav" class="owl-nav"></div>
		</div>
		
		<div class="page-heading">
			<div class="container">
				<!-- <h2>Ações de formação - Inscrições abertas</h2> -->
				<!-- <h2>Ações de formação - <span style="color: green;">Inscrições abertas</span></h2> -->
				<h2>Ações de formação <span class="flashing-text" style="animation: blink 2s infinite; color: green;">Inscrições abertas</span></h2>
				
			</div>
		</div>
		<!-- Popular courses End -->
		<div class="learn-courses">
			<div class="container" id="formacaocurso">
				<div class="courses" >
					<div class="owl-one owl-carousel">
'''
str_data_atualizacao = linha_data_atualizacao
str_html_intermediate = ''' </div>
				</div>
			</div>
		</div>
		<section class="page-heading">
			<div class="container">
				<h2>Agrupamentos de escolas públicas do concelho da Amadora</h2>
			</div>
		</section>
		<section class="gallery-images-section" itemprop="image" itemscope itemtype=" http://schema.org/ImageGallery">
			<div class="gallery-img-wrap">
				<a href="https://www.aealfornelos.ccems.pt" target="_blank">
					<img src="images/alfornelos.jpg" alt="gallery-images" data-lightbox="example-set" data-title="Click no lado direito da imagem para prosseguir ao Agrupamento seguinte ou ir para o Agrupamento Escolas.">
				</a>
				<p>
					Ir para o <a href="https://www.aealfornelos.ccems.pt" target="_blank">Agrupamento de Escolas</a>.
				</p>
			</div>
			
			
			<div class="gallery-img-wrap">
				<a href="images/ae2.jpg" data-lightbox="example-set" data-title="Click no meio lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae2.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae3.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae3.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae4.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae4.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae5.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae5.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae6.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae6.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae7.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae7.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae8.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae8.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae9.jpg" data-lightbox="example-set" data-title="Click o meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae9.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae10.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae10.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae11.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae11.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae12.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae12.jpg" alt="gallery-images">
				</a>
			</div>
		</section>
		
		<section class="query-section">
			<div class="container">
				<!-- <p>Para qualquer questão, contacte-nos através <a href="tel: 214 906 462"><i class="fas fa-phone"></i>  214 906 462</a></p> -->
			</div>
		</section>
		<!-- End of Query Section -->
		<footer class="page-footer" id="contacto">
			<div class="footer-first-section">
				<div class="container">
					<div class="box-wrap">
						<header>
							<h1>Acerca</h1>
						</header>
						<p>A CFAECA é o Centro de Formação da Associação de Escolas do Concelho da Amadora, com responsabilidade pela 
							disponibilização de ações de formação, no âmbito da formação contínua dos docentes dos Agrupamentos de Escolas.</p>
					
						<h4><a href="tel:214906462"><i class="fas fa-phone"></i>  214906462</a></h4>
						<h4><a href="mailto:director@cfaeca.org"><i class="fas fa-envelope"></i> director@cfaeca.org</a></h4>
						<h4><a href="mailto:geral@cfaeca.org"><i class="fas fa-envelope"></i> geral@cfaeca.org</a></h4>
						
						<!-- Adicionando link para Google Maps com as coordenadas -->
						<h4><a href="https://www.google.com/maps/search/?api=1&query=38.74243501375981,-9.216476282744633" target="_blank"><i class="fas fa-map-marker-alt"></i>Rua Maria Lamas, 2720-364 Amadora, Portugal</a></h4>
					</div>
					

					<div class="box-wrap">
						<header>
							<h1>Links de entidades Institucionais</h1>
						</header>
						<ul>
							<li><a href="https://www.dgeste.mec.pt/">Direção Geral dos Estabelecimentos Escolares</a></li>
							<li><a href="https://www.dgae.mec.pt/">Direção Geral da Administração Escolar</a></li>
							<li><a href="https://www.dge.mec.pt/">Direção Geral da Educação</a></li>
							<li><a href="https://www.anqep.gov.pt/np4/home">Agência Nacional para a Qual. e Ensino Profissional</a></li>
							<li><a href="https://erte.dge.mec.pt/">Equipa de Recursos e Tecnologias Educativas</a></li>
							<li><a href="https://moodle2020.cfaeca.org/">Plataforma de formação Moodle</a></li>
							<li><a href="https://www.office.com/" title="Nota:Necessário credenciais específicas distintas da Plataforma Moodle">Plataforma de formação M365Edu</a></li>
						</ul>
					</div>

					<div class="box-wrap">
						<header>
							<h1>Formações recentes</h1>
						</header>
						<div class="recent-course-wrap">
							<a href="https://www.cfaeca.pt/docs/lista_acoes_candidatura_pf2023.pdf" target="_blank">
							    <img src="images/ui-ux.jpg" alt="Ui/Ux Designing">
							      <div class="course-name">
								    <h3>Formações creditadas docentes</h3>
								    <p>já realizadas</p>
							     </div>
						   </a>
						</div>
						<div class="recent-course-wrap">
							<a href="https://digital.dge.mec.pt/capacitacao-digital-dos-docentes" target="_blank">
								<img src="images/ui-ux.jpg" alt="Ui/Ux Designing">
								<div class="course-name">
									<h3>Capacitação digital de docentes</h3>
									<p>Nível 1,2,3</p>
								</div>
							</a>
						</div>
						
					</div>

					<div class="box-wrap">
						<header>
							<h1>Parceiros</h1>
						</header>
						<ul>
							<li><a href="https://educa.cm-amadora.pt/">Câmara Municipal da Amadora</a></li>
							<li><a href="https://www.eselx.ipl.pt/">Escola Superior de Educação de Lisboa</a></li>
							<li><a href="https://www.ie.ulisboa.pt/">Instituto de Educação da Universidade de Lisboa</a></li>
						</ul>
					</div>

				</div>
			</div>
			<!-- End of box-Wrap -->
			<div class="footer-second-section">
				<div class="container">
					<hr class="footer-line">
					
					<hr class="footer-line">
				</div>
			</div>
			<div class="footer-last-section">
				<div class="container">
				
		<ul style="list-style-type: none; padding: 0;">
        <li style="display: inline; margin-right: 20px;"><a href="docs/cookies.pdf" target="_blank" style="color: white; font-size: 16px;">Cookies</a></li>
        <li style="display: inline; margin-right: 20px;"><a href="docs/termos_de_uso.pdf" target="_blank" style="color: white; font-size: 16px;">Termos de Utilização</a></li>
        <li style="display: inline;"><a href="docs/politica_de_privacidade.pdf" target="_blank" style="color: white; font-size: 16px;">Política de Privacidade</a></li>
    </ul>
      <li style="display: inline;"><a href="docs/politica_de_privacidade.pdf" target="_blank" style="color: white; font-size: 14px;">Copyright 2023-2024 &copy; CFAECA Theme designed and developed by Lab Theme e adaptado por Fernando Campos - CFAECA
		</a></li>'''
str_html_end = '''
				</div>
			</div>
		</footer>
	</div>
	<script type="text/javascript" src="js/jquery-3.3.1.min.js"></script>
	<script type="text/javascript" src="js/lightbox.js"></script>
	<script type="text/javascript" src="js/all.js"></script>
	<script type="text/javascript" src="js/owl.carousel.js"></script>
	<script type="text/javascript" src="js/jquery.flexslider.js"></script>
	<script type="text/javascript" src="js/jquery.rateyo.js"></script>
	<script type="text/javascript" src="js/isotope.pkgd.min.js"></script>
	<script type="text/javascript" src="js/jquery.mmenu.all.js"></script>
	<script type="text/javascript" src="js/custom.js"></script>
</body>
</html> '''
str_html_final = "".join([str_html_intermediate, str_data_atualizacao, str_html_end])
str_html_final2 = '''
			</div>
				</div>
			</div>
		</div>
		<section class="page-heading">
			<div class="container">
				<h2>Agrupamentos de escolas públicas do concelho da Amadora</h2>
			</div>
		</section>
		<section class="gallery-images-section" itemprop="image" itemscope itemtype=" http://schema.org/ImageGallery">
			<div class="gallery-img-wrap">
				<a href="https://www.aealfornelos.ccems.pt" target="_blank">
					<img src="images/alfornelos.jpg" alt="gallery-images" data-lightbox="example-set" data-title="Click no lado direito da imagem para prosseguir ao Agrupamento seguinte ou ir para o Agrupamento Escolas.">
				</a>
				<p>
					Ir para o <a href="https://www.aealfornelos.ccems.pt" target="_blank">Agrupamento de Escolas</a>.
				</p>
			</div>
			
			
			<div class="gallery-img-wrap">
				<a href="images/ae2.jpg" data-lightbox="example-set" data-title="Click no meio lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae2.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae3.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae3.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae4.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae4.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae5.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae5.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae6.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae6.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae7.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae7.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae8.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae8.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae9.jpg" data-lightbox="example-set" data-title="Click o meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae9.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae10.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae10.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae11.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae11.jpg" alt="gallery-images">
				</a>
			</div>
			<div class="gallery-img-wrap">
				<a href="images/ae12.jpg" data-lightbox="example-set" data-title="Click no meio  lado direito da imagem para prosseguir ao Agrupamento seguinte.">
					<img src="images/ae12.jpg" alt="gallery-images">
				</a>
			</div>
		</section>
		
		<section class="query-section">
			<div class="container">
				<!-- <p>Para qualquer questão, contacte-nos através <a href="tel: 214 906 462"><i class="fas fa-phone"></i>  214 906 462</a></p> -->
			</div>
		</section>
		<!-- End of Query Section -->
		<footer class="page-footer" id="contacto">
			<div class="footer-first-section">
				<div class="container">
					<div class="box-wrap">
						<header>
							<h1>Acerca</h1>
						</header>
						<p>A CFAECA é o Centro de Formação da Associação de Escolas do Concelho da Amadora, com responsabilidade pela 
							disponibilização de ações de formação, no âmbito da formação contínua dos docentes dos Agrupamentos de Escolas.</p>
					
						<h4><a href="tel:214906462"><i class="fas fa-phone"></i>  214906462</a></h4>
						<h4><a href="mailto:director@cfaeca.org"><i class="fas fa-envelope"></i> director@cfaeca.org</a></h4>
						<h4><a href="mailto:geral@cfaeca.org"><i class="fas fa-envelope"></i> geral@cfaeca.org</a></h4>
						
						<!-- Adicionando link para Google Maps com as coordenadas -->
						<h4><a href="https://www.google.com/maps/search/?api=1&query=38.74243501375981,-9.216476282744633" target="_blank"><i class="fas fa-map-marker-alt"></i>Rua Maria Lamas, 2720-364 Amadora, Portugal</a></h4>
					</div>
					

					<div class="box-wrap">
						<header>
							<h1>Links de entidades Institucionais</h1>
						</header>
						<ul>
							<li><a href="https://www.dgeste.mec.pt/">Direção Geral dos Estabelecimentos Escolares</a></li>
							<li><a href="https://www.dgae.mec.pt/">Direção Geral da Administração Escolar</a></li>
							<li><a href="https://www.dge.mec.pt/">Direção Geral da Educação</a></li>
							<li><a href="https://www.anqep.gov.pt/np4/home">Agência Nacional para a Qual. e Ensino Profissional</a></li>
							<li><a href="https://erte.dge.mec.pt/">Equipa de Recursos e Tecnologias Educativas</a></li>
							<li><a href="https://moodle2020.cfaeca.org/">Plataforma de formação Moodle</a></li>
							<li><a href="https://www.office.com/" title="Nota:Necessário credenciais específicas distintas da Plataforma Moodle">Plataforma de formação M365Edu</a></li>
						</ul>
					</div>

					<div class="box-wrap">
						<header>
							<h1>Formações recentes</h1>
						</header>
						<div class="recent-course-wrap">
							<a href="https://www.cfaeca.pt/docs/lista_acoes_candidatura_pf2023.pdf" target="_blank">
							    <img src="images/ui-ux.jpg" alt="Ui/Ux Designing">
							      <div class="course-name">
								    <h3>Formações creditadas docentes</h3>
								    <p>já realizadas</p>
							     </div>
						   </a>
						</div>
						<div class="recent-course-wrap">
							<a href="https://digital.dge.mec.pt/capacitacao-digital-dos-docentes" target="_blank">
								<img src="images/ui-ux.jpg" alt="Ui/Ux Designing">
								<div class="course-name">
									<h3>Capacitação digital de docentes</h3>
									<p>Nível 1,2,3</p>
								</div>
							</a>
						</div>
						
					</div>

					<div class="box-wrap">
						<header>
							<h1>Parceiros</h1>
						</header>
						<ul>
							<li><a href="https://educa.cm-amadora.pt/">Câmara Municipal da Amadora</a></li>
							<li><a href="https://www.eselx.ipl.pt/">Escola Superior de Educação de Lisboa</a></li>
							<li><a href="https://www.ie.ulisboa.pt/">Instituto de Educação da Universidade de Lisboa</a></li>
						</ul>
					</div>

				</div>
			</div>
			<!-- End of box-Wrap -->
			<div class="footer-second-section">
				<div class="container">
					<hr class="footer-line">
					
					<hr class="footer-line">
				</div>
			</div>
			<div class="footer-last-section">
				<div class="container">
				
		<ul style="list-style-type: none; padding: 0;">
        <li style="display: inline; margin-right: 20px;"><a href="docs/cookies.pdf" target="_blank" style="color: white; font-size: 16px;">Cookies</a></li>
        <li style="display: inline; margin-right: 20px;"><a href="docs/termos_de_uso.pdf" target="_blank" style="color: white; font-size: 16px;">Termos de Utilização</a></li>
        <li style="display: inline;"><a href="docs/politica_de_privacidade.pdf" target="_blank" style="color: white; font-size: 16px;">Política de Privacidade</a></li>
    </ul>
      <li style="display: inline;"><a href="docs/politica_de_privacidade.pdf" target="_blank" style="color: white; font-size: 14px;">Copyright 2023-2024 &copy; CFAECA Theme designed and developed by Lab Theme e adaptado por Fernando Campos - CFAECA
		</a></li>
		 
   		
				</div>
			</div>
		</footer>
	</div>
	<script type="text/javascript" src="js/jquery-3.3.1.min.js"></script>
	<script type="text/javascript" src="js/lightbox.js"></script>
	<script type="text/javascript" src="js/all.js"></script>
	<script type="text/javascript" src="js/owl.carousel.js"></script>
	<script type="text/javascript" src="js/jquery.flexslider.js"></script>
	<script type="text/javascript" src="js/jquery.rateyo.js"></script>
	<script type="text/javascript" src="js/isotope.pkgd.min.js"></script>
	<script type="text/javascript" src="js/jquery.mmenu.all.js"></script>
	<script type="text/javascript" src="js/custom.js"></script>
</body>
</html>
'''