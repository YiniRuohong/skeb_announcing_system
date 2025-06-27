function App() {
  const [artists, setArtists] = React.useState([]);

  React.useEffect(() => {
    fetch('/api/artists')
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
      artists.map(a =>
        React.createElement('li', { key: a.screen_name }, `${a.name} - ${a.acceptable ? 'Open' : 'Closed'}`)
      )
    )
  );
}

ReactDOM.render(React.createElement(App), document.getElementById('root'));
