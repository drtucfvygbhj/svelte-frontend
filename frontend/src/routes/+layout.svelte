<svelte:head>
  <title>My App</title>
</svelte:head>

<div class="container">
  <slot />
</div>

<style>
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
</style>