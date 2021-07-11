<template>
  <section>
      <div class="name">
          <h1>Carlos Amaral</h1>
      </div>

      <div class="description">
          <h5>Hacking...</h5>
      </div>
  </section>
</template>

<script>
export default {
    name: 'User'
}
</script>

<style scoped>
:root{
    --light: #fff;
    --dark: #242424;
    --semi-dark: #454545;
    --primary: #f93;

    --radius: 15px;
}

*{
    margin: 0;
    padding: 0;
}

section{
    background: var(--light);
    padding-left: 3em;
    padding-top: 1em;
}

section div.name{
    font-family: 'Segoe UI';
    font-size: 1rem;
    color: var(--dark)
}

section div.description{
    font-family: 'Segoe UI ';
    color: var(--semi-dark);

}
</style>