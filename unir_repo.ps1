
$repositorios = @{
    "atividade1" = "https://github.com/vinanit/Atividade-1-Fisica-Computacional.git"
    "atividade2" = "https://github.com/vinanit/Atividade-2-Fisica-Computacional.git"
    "atividade3" = "https://github.com/vinanit/Atividade-3-Fisica-Computacional.git"
    "atividade4" = "https://github.com/vinanit/Atividade_4_Fisica_computacional.git"
    "atividade5" = "https://github.com/vinanit/Atividade-5-Fisica-Computacional.git"
    "atividade6" = "https://github.com/vinanit/Atividade-6-Fisica-Computacional.git"
    "atividade7" = "https://github.com/vinanit/Atividade-7-Fisica-Computacional.git"
    "atividade8" = "https://github.com/vinanit/Atividade-8-Fisica-Computacional.git"
    "artigo" = "https://github.com/vinanit/Artigo-Fisica-Computacional.git"
}

foreach ($item in $repositorios.GetEnumerator()) {
    $pasta = $item.Key
    $url = $item.Value
    
    Write-Host "Processando $pasta..." -ForegroundColor Yellow
    git remote add temp_$pasta $url
    git fetch temp_$pasta
    git read-tree --prefix=$pasta/ -u temp_$pasta/main
    git remote remove temp_$pasta
    git commit -m "🔬 Adiciona $pasta"
    Write-Host "✅ $pasta concluído" -ForegroundColor Green
}

Write-Host "🎉 TODOS os repositórios foram adicionados!" -ForegroundColor Cyan