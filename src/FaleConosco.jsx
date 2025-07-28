import { useState } from 'react';

export default function FaleConosco() {
  const [status, setStatus] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const dados = {
      nome: e.target.nome.value,
      email: e.target.email.value,
      mensagem: e.target.mensagem.value,
    };

    try {
      const resposta = await fetch('http://127.0.0.1:5000/enviar-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados),
      });

      const resultado = await resposta.json();
      setStatus(resultado.message);
      e.target.reset();
    } catch {
      setStatus('Erro ao enviar. Tente novamente mais tarde.');
    }
  };

  return (
    <section className="faleConosco">
      <h2>Fale Conosco</h2>
      <form className="formulario" onSubmit={handleSubmit}>
        <input type="text" name="nome" placeholder="Seu nome" required />
        <input type="email" name="email" placeholder="Seu e-mail" required />
        <textarea name="mensagem" placeholder="Sua mensagem" required></textarea>
        <button type="submit">Enviar</button>
      </form>
      {status && <p>{status}</p>}
    </section>
  );
}
