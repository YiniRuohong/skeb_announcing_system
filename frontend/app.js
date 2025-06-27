function ArtistsTable({ artists }) {
  return React.createElement(
    'table',
    { className: 'artist-table' },
    React.createElement(
      'thead',
      null,
      React.createElement(
        'tr',
        null,
        React.createElement('th', null, 'Artist'),
        React.createElement('th', null, 'Open'),
        React.createElement('th', null, 'Price')
      )
    ),
    React.createElement(
      'tbody',
      null,
      artists.map(a => {
        const price = a.skills && a.skills[0] && a.skills[0].default_amount;
        const statusEmoji = a.acceptable ? '✅' : '❌';
        const priceCell = a.acceptable ? price || '?' : '-';
        return React.createElement(
          'tr',
          { key: a.screen_name },
          React.createElement('td', null, a.name),
          React.createElement('td', { className: a.acceptable ? 'status open' : 'status closed' }, statusEmoji),
          React.createElement('td', null, priceCell)
        );
      })
    )
  );
}

function App() {
  const [artists, setArtists] = React.useState([]);

  React.useEffect(() => {
    fetch('/api/artists')
      .then(res => res.json())
      .then(data => setArtists(data));
  }, []);

  return React.createElement(
    'div',
    { className: 'container' },
    React.createElement('h1', null, 'Followed Artists'),
    React.createElement(ArtistsTable, { artists })
  );
}

ReactDOM.render(React.createElement(App), document.getElementById('root'));
