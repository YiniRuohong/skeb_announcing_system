function App() {
  const [artists, setArtists] = React.useState([]);

  React.useEffect(() => {
    const base = window.location.origin.startsWith('file://')
      ? 'http://localhost:5000'
      : window.location.origin;
    fetch(base + '/api/artists')
      .then(res => res.json())
      .then(data => setArtists(data));
  }, []);

  return React.createElement(
    'div',
    null,
    React.createElement('h1', null, 'Followed Artists'),
    React.createElement(
      'ul',
      null,
      artists.map(a => {
        const price = a.skills && a.skills[0] && a.skills[0].default_amount;
        const status = a.acceptable ? `Open - Price: ${price || '?'}` : 'Closed';
        return React.createElement('li', { key: a.screen_name }, `${a.name} - ${status}`);
      })
    )
  );
}

ReactDOM.render(React.createElement(App), document.getElementById('root'));
